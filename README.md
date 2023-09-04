# Restaurant Reviews

REST API using Django REST Framework.

## Install
Create and activate virtual environment.

    python3 -m venv env
    source env/bin/activate

Install python packages.

    pip install -r requirements.txt

Create and push migrations

    python manage.py makemigrations apiv2
    python manage.py migrate
## Seed the Database
Insert a few examples of pre-scraped restaurant reviews from `Napoli Pizza` and `Canter's Deli`.

The corresponding platform ids for Napoli and Canters are `2058686` and `411068` respectively.

    python manage.py loaddata seed_fixtures.json

## Run
Run the server and visit the displayed URL [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

    python manage.py runserver

## Automate Data Updates
To update the database with the latest reviews at any given time, use the custom Django Command found in `/api/management/commands/`. The `pullreviews` command can be executed as follows: <span style="color:blue">some *blue* text</span>

    python manage.py pullreviews all
    
## API Endpoints
The following endpoints define simple behavior for our API.

`POST /restaurants`

    Creates a new Restaurant record.

`POST: /restaurants/<int:pk>/reviews`

    Creates a new Review record for the specified Restaurant.

`GET: /restaurants`

    Returns a list of all Restaurant records.

`GET: /restaurants/<int:pk>`

    Returns details about the specific Restaurant.

`GET: /restaurants/<int:pk>/reviews`

    Returns a list of all Review records for the specified Restaurant.

`GET: /restaurants/<int:pk>/reviews/<int:id>`

    Returns details about a specific Review for the corresponding Restaurant.

`PUT: /restaurants/<int:pk>`

    Updates specified Restaurant record.

`PUT: /restaurants/<int:pk>/reviews/<int:id>`

    Updates a Review record for the specified Restaurant.

`DELETE: /restaurants/<int:pk>`

    Deletes the specified Restaurant record.

`DELETE: /restaurants/<int:pk>/reviews/<int:id>`

    Deletes a Review record for the specified Restaurant.

## TODO
- [X] Add API endpoint documentation
- [X] Add class based views
- [X] Add model serializers
- [X] Add Review API endpoints
  - [X] Add create review functionality (POST)
  - [X] Add read all/detail review functionality (GET)
  - [X] Add update review functionality (PUT)
  - [X] Add delete recreviewipe functionality (DELETE)
- [X] Update API endpoints with Restaurant functionality
- [X] Add pagination
- [X] Add session management
- [X] Add search filtering
- [ ] Deploy
