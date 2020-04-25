
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from api import create_app
from models import setup_db, Actor, Movie, db_drop_and_create_all
from config import Test


class CastingTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.new_actor = {
            "name": "John Doe",
            "age": 35,
            "gender": "male"
        }
        self.new_actor2 = {
            "name": "Jane Doe",
            "age": 25,
            "gender": "female"
        }
        self.new_movie = {
            "title": "Hard die 1",
            "release_date": "1980-04-22 10:04:29"
        }
        self.new_movie2 = {
            "title": "Hard die 2",
            "release_date": "1985-04-22 10:04:29"
        }
        self.header_assistant = {
            'Authorization': 'Bearer ' + Test.token_assistant}
        self.header_director = {
            'Authorization': 'Bearer ' + Test.token_director}
        self.header_producer = {
            'Authorization': 'Bearer ' + Test.token_producer}

        self.database_path = Test.database_url_test

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            db_drop_and_create_all()
            actor = Actor(**self.new_actor)
            actor.insert()
            movie = Movie(**self.new_movie)
            movie.insert()

    def tearDown(self):
        """Executed after reach test"""
        db_drop_and_create_all()
        actor = Actor(**self.new_actor)
        actor.insert()
        movie = Movie(**self.new_movie)
        movie.insert()

    def test_home(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_actors_public(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    # ----------------------------------------------------------------------------#
    # Assistant.
    # ----------------------------------------------------------------------------#

    def test_get_actors_assistant(self):
        res = self.client().get('/actors', headers=self.header_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_create_new_actor_assistant(self):
        res = self.client().post(
            '/actors',
            headers=self.header_assistant,
            json=self.new_actor2)
        self.assertEqual(res.status_code, 401)

    def test_update_actor_assistant(self):
        res = self.client().patch(
            '/actors/1',
            headers=self.header_assistant,
            json=self.new_actor2)
        self.assertEqual(res.status_code, 401)

    def test_delete_actor_assistant(self):
        res = self.client().delete('/actors/1', headers=self.header_assistant)
        self.assertEqual(res.status_code, 401)

    def test_get_movies_assistant(self):
        res = self.client().get('/movies', headers=self.header_assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_create_new_movie_assistant(self):
        res = self.client().post(
            '/movies',
            headers=self.header_assistant,
            json=self.new_movie2)
        self.assertEqual(res.status_code, 401)

    def test_update_movie_assistant(self):
        res = self.client().patch(
            '/movies/1',
            headers=self.header_assistant,
            json=self.new_movie2)
        self.assertEqual(res.status_code, 401)

    def test_delete_movie_assistant(self):
        res = self.client().delete('/movies/1', headers=self.header_assistant)
        self.assertEqual(res.status_code, 401)

    # ----------------------------------------------------------------------------#
    # Director.
    # ----------------------------------------------------------------------------#

    def test_get_actors_director(self):
        res = self.client().get('/actors', headers=self.header_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_create_new_actor_director(self):
        res = self.client().post(
            '/actors',
            headers=self.header_director,
            json=self.new_actor2)
        self.assertEqual(res.status_code, 200)

    def test_update_actor_director(self):
        res = self.client().patch(
            '/actors/1',
            headers=self.header_director,
            json=self.new_actor2)
        self.assertEqual(res.status_code, 200)

    def test_delete_actor_director(self):
        res = self.client().delete('/actors/1', headers=self.header_director)
        self.assertEqual(res.status_code, 200)

    def test_get_movies_director(self):
        res = self.client().get('/movies', headers=self.header_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_create_new_movie_director(self):
        res = self.client().post(
            '/movies',
            headers=self.header_director,
            json=self.new_movie2)
        self.assertEqual(res.status_code, 200)

    def test_update_movie_director(self):
        res = self.client().patch(
            '/movies/1',
            headers=self.header_director,
            json=self.new_movie2)
        self.assertEqual(res.status_code, 200)

    def test_delete_movie_director(self):
        res = self.client().delete('/movies/1', headers=self.header_director)
        self.assertEqual(res.status_code, 401)

    # ----------------------------------------------------------------------------#
    # Producer.
    # ----------------------------------------------------------------------------#

    def test_get_actors_producer(self):
        res = self.client().get('/actors', headers=self.header_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_create_new_actor_producer(self):
        res = self.client().post(
            '/actors',
            headers=self.header_producer,
            json=self.new_actor2)
        self.assertEqual(res.status_code, 200)

    def test_update_actor_producer(self):
        res = self.client().patch(
            '/actors/1',
            headers=self.header_producer,
            json=self.new_actor2)
        self.assertEqual(res.status_code, 200)

    def test_delete_actor_producer(self):
        res = self.client().delete('/actors/1', headers=self.header_producer)
        self.assertEqual(res.status_code, 200)

    def test_get_movies_producer(self):
        res = self.client().get('/movies', headers=self.header_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_create_new_movie_producer(self):
        res = self.client().post(
            '/movies',
            headers=self.header_producer,
            json=self.new_movie2)
        self.assertEqual(res.status_code, 200)

    def test_update_movie_producer(self):
        res = self.client().patch(
            '/movies/1',
            headers=self.header_producer,
            json=self.new_movie2)
        self.assertEqual(res.status_code, 200)

    def test_delete_movie_producer(self):
        res = self.client().delete('/movies/1', headers=self.header_producer)
        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
