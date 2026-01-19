from pprint import pprint


class TestBaseView:
    def test_status_code_ok_hp(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_login(self, client):
        email = 'testEmail'
        password = 'testPassword'
        headers = {'Content-Type': 'application/json'}
        response = client.post('/api/login', headers=headers, json={'email': email, 'password': password})
        pprint(response.data)
        assert response.status_code == 200

    def test_login_missing_email(self, client):
        headers = {'Content-Type': 'application/json'}
        response = client.post('/api/login', headers=headers, json={'password': 'testPassword'})
        assert response.status_code in [400, 422]

    def test_login_missing_password(self, client):
        headers = {'Content-Type': 'application/json'}
        response = client.post('/api/login', headers=headers, json={'email': 'testEmail'})
        assert response.status_code in [400, 422]

    def test_login_invalid_credentials(self, client):
        headers = {'Content-Type': 'application/json'}
        response = client.post('/api/login', headers=headers, json={'email': 'invalid@test.com', 'password': 'wrongpass'})
        assert response.status_code in [401, 403]

    def test_login_empty_payload(self, client):
        headers = {'Content-Type': 'application/json'}
        response = client.post('/api/login', headers=headers, json={})
        assert response.status_code in [400, 422]

