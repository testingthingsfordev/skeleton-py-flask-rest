from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from api.resources.health import Health
from api.resources.welcome import Welcome


def create_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:password@flask-db/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    db.create_all()

    return db


def create_api():
    app = Flask(__name__)
    db = create_db(app)

    api = Api(app)

    api.add_resource(Welcome, '/')
    api.add_resource(Health, '/health', resource_class_kwargs={'db': db})

    return api
