from flask import render_template
from app.web.auth import bp


@bp.route('/login')
def login():
    return render_template('auth/login.html')
