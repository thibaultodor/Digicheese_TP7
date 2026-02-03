"""Tests for authentication functionality."""


class TestAuth:
    """Test cases for authentication routes."""

    def test_not_redirecting_to_login(self, client):
        """Test authentication requirement for protected routes."""
        response = client.get("/admin/users/", follow_redirects=True)

        # Check redirect to login page when not logged in
        assert "?next=/admin/users/" not in response.request.url
        assert response.status_code == 401

    def test_authentication_json(self, client):
        """Test JSON authentication endpoint."""
        with client:
            response = client.post(
                "/api-login",
                headers={"Content-Type": "application/json"},
                json={"email": "admin@test.com", "password": "admin123"},
            )
        assert response.json.get("id") == 1
        assert response.json.get("name") == "admin"
        assert response.json.get("email") == "admin@test.com"
        assert response.status_code == 200

    def test_page_needing_login(self, authenticated_admin_client):
        """Test accessing page that requires authentication."""
        response = authenticated_admin_client.get("/profile")
        assert "Welcome, admin" in response.get_data(as_text=True)

    # TEST LOGOUT
    def test_logout(self, authenticated_admin_client):
        """Test logout functionality."""
        response = authenticated_admin_client.get("/api-logout", follow_redirects=True)
        assert "Logged out successfully" in response.get_data(as_text=True)
        assert response.status_code == 200
