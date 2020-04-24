import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#


def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    # ----------------------------------------------------------------------------#
    # Routes.
    # ----------------------------------------------------------------------------#

    @app.route('/')
    def home():
        return 'Full Stack Casting Agency API Backend'

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(token):
        try:
            actors = [actor.format() for actor in Actor.query.all()]
            return jsonify({
                'success': True,
                'actors': actors
            }), 200
        except Exception:
            abort(404)

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(token):
        try:
            movies = [movie.format() for movie in Movie.query.all()]
            return jsonify({
                'success': True,
                'movies': movies
            }), 200
        except Exception:
            abort(404)

    @app.route("/actors", methods=['POST'])
    @requires_auth('post:actors')
    def add_actors(token):
        try:
            data = request.get_json()
            name = data.get('name', None)
            age = data.get('age', None)
            gender = data.get('gender', None)
            actor = Actor(name=name, age=age, gender=gender)
            actor.insert()
            new_actor = Actor.query.filter_by(id=actor.id).first()
            new_actor = new_actor.format()
            return jsonify({'success': True, 'actor': new_actor})
        except Exception:
            abort(422)

    @app.route("/movies", methods=['POST'])
    @requires_auth('post:movies')
    def add_movies(token):
        try:
            data = request.get_json()
            title = data.get('title', None)
            release_date = data.get('release_date', None)
            movie = Movie(title=title, release_date=release_date)
            movie.insert()
            new_movie = Movie.query.filter_by(id=movie.id).first()
            new_movie = new_movie.format()
            return jsonify({'success': True, 'movie': new_movie})
        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actor(token, actor_id):
        try:
            data = request.get_json()
            actor = Actor.query.filter_by(id=actor_id).one_or_none()
            if actor is None:
                abort(404)
            if 'name' in data:
                actor.name = data.get('name')
            if 'age' in data:
                actor.age = data.get('age')
            if 'gender' in data:
                actor.gender = data.get('gender')
            actor.update()
            return jsonify({
                'success': True,
                'actors': [actor.format()]
            })
        except Exception:
            abort(404)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movie(token, movie_id):
        try:
            data = request.get_json()
            movie = Movie.query.filter_by(id=movie_id).one_or_none()
            if movie is None:
                abort(404)
            if 'title' in data:
                movie.title = data.get('title')
            if 'release_date' in data:
                movie.release_date = data.get('release_date')
            movie.update()
            return jsonify({
                'success': True,
                'movies': [movie.format()]
            })
        except Exception:
            abort(404)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(token, actor_id):
        try:
            actor = Actor.query.filter_by(id=actor_id).one_or_none()
            if actor is None:
                abort(404)
            actor.delete()
            return jsonify({
                'success': True,
                'deleted': actor_id
            })
        except Exception:
            abort(404)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(token, movie_id):
        try:
            movie = Movie.query.filter_by(id=movie_id).one_or_none()
            if movie is None:
                abort(404)
            movie.delete()
            return jsonify({
                'success': True,
                'deleted': movie_id
            })
        except Exception:
            abort(404)

    # ----------------------------------------------------------------------------#
    # Error Handling.
    # ----------------------------------------------------------------------------#

    @app.errorhandler(400)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }, 405)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'
        }, 500)

    # ----------------------------------------------------------------------------#
    # Error handler for AuthError.
    # ----------------------------------------------------------------------------#

    @app.errorhandler(AuthError)
    def auth_error(e):
        return jsonify(e.error), e.status_code

    return app
