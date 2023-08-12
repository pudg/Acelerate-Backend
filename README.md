# Acelerate Backend

## Install
Create and activate virtual environment.

    python3 -m venv env
    source env/bin/activate

Install python packages.

    pip install -r requirements.txt

Create and push migrations

    python manage.py makemigrations api
    python manage.py migrate api
## Seed the Database
Insert a few examples of pre-scraped restaurant reviews from `Napoli Pizza` and `Canter's Deli`.

The corresponding platform ids for Napoli and Canters are `2058686` and `411068` respectively.

    # Seed the database.
    python manage.py loaddata seed_fixtures.json

    

## Run
Run the server and visit the displayed URL [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

    python manage.py runserver

## Automate Data Updates
To update the database with the latest reviews at any given time use the custom Django command found in `/api/management/commands/`. The `pullreviews` comman can be executed from Django directly using

    django manage.py pullreviews all
    
## API Endpoints
The following endpoints define simple behavior for our API.

`/api` 

    Returns a list of all available restaurant platform providers. (i.e. grubhub, ubereats, doordash)
    Open the following link to view the results.

    http://127.0.0.1:8000/api



`/api/<str:platform>/restaurant/<int:identifier>/reviews`

    Returns a list of all reviews from the specified `platform` for the restaurant `identifier`.
    Open the following link to view a list of all results for reviews for Napoli Pizza

    http://127.0.0.1:8000/api/grubhub/restaurant/2058686/reviews

`/api/<str:platform>/restaurant/<int:identifier>/problematic`

    Returns a list of all items rated with less than three stars from the specified `platform` for the 
    restaurant `identifier`. Open the following link to view a list of all problematic items from Napoli
    Pizza.

    http://127.0.0.1:8000/api/grubhub/restaurant/2058686/problematic

`/api/<str:platform>/restaurant/<int:identifier>/best`

    Returns a list of all items with five-star rating from the specified `platform` for the restaurant `identifier`. Open the following link to view a list of all five-star rated items from Napoli Pizza.

    http://127.0.0.1:8000/api/grubhub/restaurant/2058686/best