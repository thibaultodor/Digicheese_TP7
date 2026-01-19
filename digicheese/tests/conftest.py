import pytest
from .. import create_app
from .. import db
from digicheese.models import Utilisateur as User

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()

        user = User(name='admin', email='admin@test.com')
        user.set_password('admin123')
        db.session.add(user)
        db.session.commit()


        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


# @pytest.fixture
# def create_admin_user(app):
#     with app.app_context():
#         user = User(name='admin', email='admin@test.com')
#         user.set_password('admin123')
#         db.session.add(user)
#         db.session.commit()
#         return user


@pytest.fixture
def regular_user(app):
    with app.app_context():
        user = User(name='user', email='user@test.com')
        user.set_password('user123')
        db.session.add(user)
        db.session.commit()
        return user
