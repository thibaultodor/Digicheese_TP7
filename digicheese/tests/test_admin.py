from pprint import pprint
from .conftest import client, regular_user
from digicheese.models import Utilisateur as User


class TestAdminRoutes:
    def test_redirect_to_login(self, client):
        response = client.get("/admin/users/", follow_redirects=True)
        pprint(vars(response.request))
        # Check redirect to login page when not logged in
        assert "?next=/admin/users/" in response.request.url
        assert response.status_code == 200


    def test_login_json(self, client):
        headers = {"Content-Type": "application/json"}
        response = client.post(
            "/api/login", 
            headers=headers, 
            json={"email": "admin@test.com", "password": "admin123"}
        )
        assert response.json.get("id") == 1
        assert response.json.get("name") == "admin"
        assert response.json.get("email") == "admin@test.com"
        assert response.status_code == 200


def test_modify_session(client):
    with client.session_transaction() as session:
        # set a user id without going through the login route
        session["user_id"] = 1

    # session is saved now

    response = client.get("/users/me")
    assert response.json["username"] == "flask"



    # def test_admin_dashboard_requires_admin(client, regular_user):
    #     client.post("/login", data={"username": "user", "password": "user123"})
    #     response = client.get("/admin/")
    #     assert response.status_code == 403


    # def test_admin_dashboard_access(client, admin_user):
    #     client.post("/login", data={"username": "admin", "password": "admin123"})
    #     response = client.get("/admin/")
    #     assert response.status_code == 200


    # def test_admin_users_list(client, admin_user):
    #     client.post("/login", data={"username": "admin", "password": "admin123"})
    #     response = client.get("/admin/users")
    #     assert response.status_code == 200


    # def test_admin_delete_user(client, admin_user, regular_user):
    #     client.post("/login", data={"username": "admin", "password": "admin123"})
    #     response = client.post(f"/admin/users/{regular_user.id}/delete")
    #     assert response.status_code in [200, 302]


    # def test_admin_cheeses_list(client, admin_user):
    #     client.post("/login", data={"username": "admin", "password": "admin123"})
    #     response = client.get("/admin/cheeses")
    #     assert response.status_code == 200


    # def test_admin_orders_list(client, admin_user):
    #     client.post("/login", data={"username": "admin", "password": "admin123"})
    #     response = client.get("/admin/orders")
    #     assert response.status_code == 200