import os

from flask import Flask

# The __init__ file serves two functions:
# 1. Contains the application factory
# 2. Tells python that flaskr directory should be treated as package
def create_app(test_config=None):

    # Create and configure the app.
    # __name__ is the name of the current Python module. The app needs
    # to know where it's located to set up some paths, and __name__ is
    # a convenient way to tell it that.
    app = Flask(__name__, instance_relative_config=True)

    # Some default configuration that the app will use.
    # SECRET_KEY is used by Flask and extensions to keep data safe.
    # It's set to 'dev' to provide a convenient value during development,
    # but it should be overridden with a random value when deploying.
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Overrides the default configuration with values taken from the
    # config.py file in the instance folder if it exists. For example,
    # when deploying, this can be used to set a real SECRET_KEY.
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, world!'

    from . import db
    db.init_app(app)

    return app
