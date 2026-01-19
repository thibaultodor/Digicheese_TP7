import pytest
from .. import create_app
from .. import db
from digicheese.models import Utilisateur as User

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def admin_user(app):
    with app.app_context():
        user = User(username='admin', email='admin@test.com', is_admin=True)
        user.set_password('admin123')
        db.session.add(user)
        db.session.commit()
        return user


@pytest.fixture
def regular_user(app):
    with app.app_context():
        user = User(username='user', email='user@test.com', is_admin=False)
        user.set_password('user123')
        db.session.add(user)
        db.session.commit()
        return user



# @pytest.fixture
# def client():
#     app = create_app()
#     with app.test_client() as client:
#         yield client