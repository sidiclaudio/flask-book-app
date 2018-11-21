# book_catalog/app/_init_.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


# Importing flask classes from module Flask
# Flask application instance


db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_type):  # dev, test, or prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    # attach to DB instance
    db.init_app(app)

    # initialize the bootstrap instance
    bootstrap.init_app(app)

    # Import main from Catalog
    from app.catalog import main
    app.register_blueprint(main)

    # import authentication from app.auth
    from app.auth import authentication
    app.register_blueprint(authentication)

    return app
