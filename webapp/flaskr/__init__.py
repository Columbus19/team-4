import os

from flask import Flask

def create_app(test_config=None):

    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev',#this should be changed to random during dev
                            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),)

    if test_config is None:

        app.config.from_pyfile('config.py', silent=True)

    else:

        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def landing_page():
        return "Welcome!"


    from . import db, auth
    db.init_app(app)

    app.register_blueprint(auth.blue_print)
    return app
