import pytest

from digicheese.enums.role_enum import RoleEnum
from digicheese.models.role import Role
from digicheese.models.roles_utilisateur import RolesUtilisateur
from .. import create_app
from .. import db
from digicheese.models import Utilisateur as User

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()

        admin = User(name='admin', email='admin@test.com')
        admin.set_password('admin123')
        colis = User(name='colis', email='colis@test.com')
        colis.set_password('colis123')
        db.session.add(admin)
        db.session.add(colis)

        role = Role(libelle=RoleEnum.ADMIN.value)
        role1 = Role(libelle=RoleEnum.COLIS.value)
        role2 = Role(libelle=RoleEnum.STOCK.value)
        db.session.add(role)
        db.session.add(role1)
        db.session.add(role2)

        role_utilisateur_admin = RolesUtilisateur(user=admin, role=role)
        role_utilisateur_colis = RolesUtilisateur(user=colis, role=role1)
        db.session.add(role_utilisateur_admin)
        db.session.add(role_utilisateur_colis)
        
        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def authenticated_admin_client(client):
    with client:
        client.post(
            "/api-login",
            headers={"Content-Type": "application/json"},
            json={"email": "admin@test.com", "password": "admin123"}
        )
        yield client

@pytest.fixture
def authenticated_package_client(client):
    """Client authenticated as a regular user"""
    with client:
        client.post(
            "/api-login",
            headers={"Content-Type": "application/json"},
            json={"email": "colis@test.com", "password": "colis123"}
        )
        yield client