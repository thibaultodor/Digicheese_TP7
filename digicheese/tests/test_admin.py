from pprint import pprint


class TestAdminRoutes:
    def test_admin_access_user_list(self, authenticated_admin_client):
        response = authenticated_admin_client.get("/admin/users/")
        pprint(response.json)
        assert response.status_code == 200
        assert isinstance(response.json, list)
        assert len(response.json) >= 2  
    
    def test_role_guard_for_non_admin(self, authenticated_package_client):
        response = authenticated_package_client.get("/admin/users/")
        assert response.status_code == 403
        assert response.json.get("error") == "Forbidden"
        