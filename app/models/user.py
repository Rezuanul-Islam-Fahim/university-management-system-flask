from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def __init__(self, username, full_name, email, password):

        self.username = username
        self.full_name = full_name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __repr__(self):

        return f'Username: {self.username}, Full Name: {self.full_name}, \
                Email: {self.email}'
