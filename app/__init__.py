"""

(c) 2019 - ModoUnreal

app/__init__.py

"""


import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    # create and configure the application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='notsosecretafterall',
        DATABASE=os.path.join(app.instance_path, 'access.sqlite'),
    )
    # Define the database instance
    db = SQLAlchemy(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing.
        app.config.from_pyfile('config.py', silent=True)

    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # This is a simple view that displays text
    @app.route('/hello')
    def hello():
        return render_template('index.html', title='Access: The Search Engine For Services')

    return app

app = create_app()
