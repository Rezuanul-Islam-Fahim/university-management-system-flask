from flask import Flask

from config import Config
from app.db import db


def create_app(config=Config):

    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from app.web import AuthBlueprint
    app.register_blueprint(AuthBlueprint, url_prefix='/auth')

    return app
