import pytest
from flask import session
from digicheese import create_app, db
from digicheese.models import Utilisateur as User



def test_admin_dashboard_requires_login(client):
    response = client.get('/admin/')
    assert response.status_code == 302


def test_admin_dashboard_requires_admin(client, regular_user):
    client.post('/login', data={'username': 'user', 'password': 'user123'})
    response = client.get('/admin/')
    assert response.status_code == 403


def test_admin_dashboard_access(client, admin_user):
    client.post('/login', data={'username': 'admin', 'password': 'admin123'})
    response = client.get('/admin/')
    assert response.status_code == 200


def test_admin_users_list(client, admin_user):
    client.post('/login', data={'username': 'admin', 'password': 'admin123'})
    response = client.get('/admin/users')
    assert response.status_code == 200


def test_admin_delete_user(client, admin_user, regular_user):
    client.post('/login', data={'username': 'admin', 'password': 'admin123'})
    response = client.post(f'/admin/users/{regular_user.id}/delete')
    assert response.status_code in [200, 302]


def test_admin_cheeses_list(client, admin_user):
    client.post('/login', data={'username': 'admin', 'password': 'admin123'})
    response = client.get('/admin/cheeses')
    assert response.status_code == 200


def test_admin_orders_list(client, admin_user):
    client.post('/login', data={'username': 'admin', 'password': 'admin123'})
    response = client.get('/admin/orders')
    assert response.status_code == 200