from flask_login import UserMixin
from . import db

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(100))
