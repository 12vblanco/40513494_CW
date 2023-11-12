from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    # secret key for the form, saved in environmental variables and fall back key for development
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fall_back')
    database_uri = 'sqlite:///bookings.db'
    import routes
    import api

# if the database needs to be created we can run create_table from here
# from models import *
# create_table()

``




# running the app using https protocol for enhance security
# https://kracekumar.com/post/54437887454/ssl-for-flask-local-development/
# key too small error, solved increasing the size https://stackoverflow.com/questions/67753969/sslerror-ssl-ee-key-too-small-ee-key-too-small-ssl-c4022-on-ubuntu-when

# to run https: flask run --cert=server.crt --key=server.key
# to run http: flask run 
    return app