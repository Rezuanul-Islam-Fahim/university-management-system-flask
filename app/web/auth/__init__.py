from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.web.auth import views