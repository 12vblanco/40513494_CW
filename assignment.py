from flask import Flask, render_template
import os
import sqlite3


# waitress was giving me a create_app error so I extracted factories and blueprints from https://flask.palletsprojects.com/en/2.3.x/patterns/appfactories/
def create_app():
    app = Flask(__name__)
    # secret key for the form, saved in environmental variables and fall back key for development
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fall_back')
    # and also blueprints from https://flask.palletsprojects.com/en/2.3.x/blueprints/
    from routes import routes_blueprint
    app.register_blueprint(routes_blueprint)

    from api import api_blueprint
    app.register_blueprint(api_blueprint)
    
    # Error handling from the workbook and https://flask.palletsprojects.com/en/2.3.x/errorhandling/
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404_error.html'), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template('500_error.html'), 500

    return app

app = create_app()

basedir = os.path.abspath(os.path.dirname(__file__))

# running the app using https protocol for enhance security
# https://kracekumar.com/post/54437887454/ssl-for-flask-local-development/
# key too small error, solved increasing the size https://stackoverflow.com/questions/67753969/sslerror-ssl-ee-key-too-small-ee-key-too-small-ssl-c4022-on-ubuntu-when

# to run https: flask run --cert=server.crt --key=server.key
# to run http: flask run 
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, ssl_context=('/server.crt', '/server.key'))  # for HTTPS
    # app.run(debug=True)  # for HTTP

