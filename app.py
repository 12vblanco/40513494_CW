from flask import Flask
import os

app = Flask(__name__)
import routes
import api

basedir = os.path.abspath(os.path.dirname(__file__))

# secret key for the form, saved in environmental variables and fall back key for development
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fall_back')


# running the app using https protocol for enhance security
# https://kracekumar.com/post/54437887454/ssl-for-flask-local-development/
# key too small error, solved increasing the size https://stackoverflow.com/questions/67753969/sslerror-ssl-ee-key-too-small-ee-key-too-small-ssl-c4022-on-ubuntu-when

# to run https: flask run --cert=server.crt --key=server.key
# to run http: flask run 
if __name__ == '__main__':
    app.run(debug=False)