from flask import Flask
from flask_migrate import Migrate

from config import Config
from app.db import db


def create_app(config=Config):

    app = Flask(__name__, template_folder='web/templates')
    app.config.from_object(config)

    db.init_app(app)
    Migrate(app, db)

    from app.web import AuthBlueprint
    app.register_blueprint(AuthBlueprint, url_prefix='/auth')

    return app
