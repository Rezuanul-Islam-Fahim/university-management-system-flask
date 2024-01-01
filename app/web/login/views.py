from app.web.login import bp


@bp.route('/login')
def login():
    return '<h1>This is login page</h1>'
