# Full Stack Casting Agency API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup
With Postgres running, install a database use the terminal running:
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run
```

## API Reference

### Getting started
Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.

### Error handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API return 5 error types when request fail:
- 400: Bad Request
- 401: Authorization Error
- 404: Resource Not Found
- 405: Method not allowed
- 422: Not Processable
- 500: Internal Server Error

### Endpoints. 

#### GET '/actors'

- Fetches a dictionary of actors
- Request Arguments: None
- Returns: An object with actors, that contains name, age, gender and id. 
- Sample :  ``` curl -X GET http://localhost:5000/actors```
```
{
    "actors": [
        {
            "age": 35,
            "gender": "female",
            "id": 2,
            "name": "Jane Doe"
        },
        {
            "age": 35,
            "gender": "male",
            "id": 1,
            "name": "John Doe"
        }
    ],
    "success": true
}
```

#### GET '/movies'

- Fetches a dictionary of movies
- Request Arguments: None
- Returns: An object with movies, that contains title, release date and id. 
- Sample :  ``` curl -X GET http://localhost:5000/movies```
```
{
    "movies": [
        {
            "id": 2,
            "release_date": "Sat, 22 Apr 2000 10:04:29 GMT",
            "title": "Hard die"
        },
        {
            "id": 1,
            "release_date": "Fri, 22 Apr 1983 10:04:29 GMT",
            "title": "Nobody will die"
        }
    ],
    "success": true
}
```

#### POST '/actors'
- Create a new actor using name, age and gender
- Returns: The new actor. 
- Sample :
```
curl -X POST http://localhost:5000/actors \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Jane Doe",
    "age": 35,
    "gender": "female"
}'
```
- Response:
```
{
    "actor": {
        "age": 35,
        "gender": "female",
        "id": 1,
        "name": "Jane Doe"
    },
    "success": true
}
```

#### POST '/movies'
- Create a new movie using title and release date
- Returns: The new movie. 
- Sample :
```
curl -X POST http://localhost:5000/movies/1 \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Hard die",
    "release_date": "2000-04-22 10:04:29"
}'
```
- Response:
```
{
    "movie": {
        "id": 12,
        "release_date": "Sat, 22 Apr 2000 10:04:29 GMT",
        "title": "Hard die"
    },
    "success": true
}
```

#### PATCH '/actors/{actor_id}'
- Update a actor using name, age or gender
- Returns: The updated actor. 
- Sample :
```
curl -X PATCH http://localhost:5000/actors/1 \
  -H 'Content-Type: application/json' \
  -d '{
    "age": 25,
    "gender": "male"
}'
```
- Response:
```
{
    "actor": {
        "age": 25,
        "gender": "male",
        "id": 1,
        "name": "Jane Doe"
    },
    "success": true
}
```

#### PATCH '/movies//{movie_id}'
- Update a movie using title or release date
- Returns: The updated movie. 
- Sample :
```
curl -X PATCH http://localhost:5000/movies/1 \
  -H 'Content-Type: application/json' \
  -d '{
     "release_date": "1988-04-22 10:04:29"
}'
```
- Response:
```
{
    "movie": {
        "id": 1,
        "release_date": "Fri, 22 Apr 1988 10:04:29 GMT",,
        "title": "Hard die"
    },
    "success": true
}
```

#### DELETE '/actors/{actor_id}'
- DELETE actor using a actor ID.
- Sample: ``` curl -X DELETE http://localhost:5000/actors/5```

```
{
    'success': True
    'deleted': 5
}
```

#### DELETE '/movies/{movie_id}'
- DELETE movie using a movie ID.
- Sample: ``` curl -X DELETE http://localhost:5000/movies/5```

```
{
    'success': True
    'deleted': 5
}
```

## Testing
Test your endpoints with [Postman](https://getpostman.com).
- Import the postman collection `./casting.postman_collection.json`
- Run the collection

## Deployment
This API is deployed in https://casting-agency-fsndcapstone.herokuapp.com/

## Authors
Dieter Jackson