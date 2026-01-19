from pprint import pprint
from digicheese.models import Utilisateur as User


class TestAdminRoutes:
    def test_redirect_to_login(self, client):
        response = client.get("/admin/users/", follow_redirects=True)

        # Check redirect to login page when not logged in
        assert "?next=/admin/users/" in response.request.url
        assert response.status_code == 200

    def test_authentication_json(self, client):
        headers = {"Content-Type": "application/json"}
        with client:
            response = client.post(
                "/api/login", 
                headers=headers, 
                json={"email": "admin@test.com", "password": "admin123"}
            )
        assert response.json.get("id") == 1
        assert response.json.get("name") == "admin"
        assert response.json.get("email") == "admin@test.com"
        assert response.status_code == 200
    
    def test_page_needing_login(self, authenticated_admin_client):
        response = authenticated_admin_client.get("/profile")
        assert "Welcome, admin" in response.get_data(as_text=True)

    





