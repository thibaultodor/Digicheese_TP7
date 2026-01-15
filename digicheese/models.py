from enum import Enum
from flask_login import UserMixin
from . import db


class MyEnum(Enum):
    ADMIN = "admin"
    COLIS = "colis"
    STOCK = "stock"


def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(100))
    role = db.Column(db.Enum(MyEnum), default=MyEnum.COLIS)

    def has_role(self, role):
        return self.role == role

