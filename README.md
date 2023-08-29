# Restaurant Reviews

REST API using Django REST Framework.

## Install
Create and activate virtual environment.

    python3 -m venv env
    source env/bin/activate

Install python packages.

    pip install -r requirements.txt

Create and push migrations

    python manage.py makemigrations api
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

## Refresh Restaurant Reviews
To directly refresh restaurant reviews from the web-app use the `Refresh` button on the top right of
[http://127.0.0.1:8000/](http://127.0.0.1:8000/).
    
## API Endpoints
The following endpoints define simple behavior for our API.

`POST /reviews`

    Creates a new Review record using given json object.

`GET: /reviews`

    Returns a list of all reviews.

`GET: /reviews/<int:pk>`

    Returns information about a specific Review.

`PUT: /reviews/<int:pk>`

    Updates specified Review record given json object.

`DELETE: /reviews/<int:pk>`

    Deletes the specified Review record.

## TODO
- [X] Add API endpoint documentation
- [ ] Add class based views
- [ ] Add model serializers
- [ ] Add API endpoints
  - [ ] Add create review functionality (POST)
  - [ ] Add read all/detail review functionality (GET)
  - [ ] Add update review functionality (PUT)
  - [ ] Add delete recreviewipe functionality (DELETE)
- [ ] Add pagination
- [ ] Add session management
- [ ] Add search filtering
- [ ] Deploy
