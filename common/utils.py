import random, json, os;
import asyncio
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
import pyppeteer


def create_header():
    """Creates a request header with a random useragent.

    Returns:
        A header with a randomly selected useragent.
    """
    useragent_file = open(os.path.join(os.getcwd(), 'common/userAgents.json'))
    useragentStrings = json.load(useragent_file)
    useragent_file.close()
    useragent = random.choice(useragentStrings)
    headers = {
        "User-Agent": useragent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }
    return headers


def parse(html):
    """Parses scraped HTML.

    Process the scraped HTML returned from request-html.

    Args:
        html:
            Scraped document HTML content.

    Returns:
        Array of review dictionary objects.
    """
    soup = BeautifulSoup(html, 'lxml')
    scripts = soup.find_all('script')
    reviews = None
    for script in scripts:
        if script.has_attr('type') and script['type'] == 'application/ld+json':
            reviews = script.text
            break
    
    if reviews and ('review' in reviews):
        reviews = json.loads(reviews)
        reviews = reviews['review']
    return reviews


async def render_html(url):
    """Scrapes the HTML from the specified site.

    Scrapes and renders the dynamic page found at the specified URL.

    Args:
        url:
            A string denoting the url path of the target website.
    
    Returns:
        Array of review dictionary objects.
    """
    asession = AsyncHTMLSession()
    browser = await pyppeteer.launch({ 
        'ignoreHTTPSErrors':False, 
        'headless': False, 
        'handleSIGINT':False, 
        'handleSIGTERM':False, 
        'handleSIGHUP':False
    })
    asession._browser = browser
    headers = create_header()
    res = await asession.get(url=url, headers=headers)
    await res.html.arender(keep_page=True, sleep=3)
    html = res.html.html
    reviews = parse(html=html)
    return reviews


def handle_review_refresh(Restaurant, Review, identifier, platform):
    """Handles for background data update process.

    In between function used to handle the review refresh process in a
    background thread.

    Args:
        Restaurant:
            Django Restaurant data model.
        
        Review:
            Django Review data model.

        identifier:
            String denoting platform specific restaurant id.

        platform:
            String denoting the provider to scrape.
    
    Returns:
        None
    """
    restaurant = Restaurant.objects.filter(platform_id=identifier)
    if restaurant:
        url = restaurant[0].uri
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        future = asyncio.ensure_future(render_html(url))
        reviews = loop.run_until_complete(future)
        loop.close()
        update_database(platform=platform, restaurant_id=restaurant[0].id, Review=Review, reviews=reviews)
    return


def update_database(platform, restaurant_id, Review, reviews):
    """Update reviews in our database.

    Populates database with the most recently scraped restaurant reviews.

    Args:
        platform:
            String denoting the provider to scrape.

        restaurant_id:
            Integer denoting the restaurant table id within database.
        
        Review:
            Django Review data model.

        reviews:
            Array of review dictionary objects.

    Returns:
        None
    """
    if reviews:
        for review in reviews:
            Review.objects.update_or_create(
                restaurant=restaurant_id,
                reviewer=review["author"],
                comment=review["reviewBody"],
                platform=platform,
                star_rating=review["reviewRating"]["ratingValue"],
                menu_items=[]
            )
    return
