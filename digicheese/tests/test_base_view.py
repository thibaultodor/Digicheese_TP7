from pprint import pprint


class TestBaseView:
    def test_status_code_ok_hp(self, client):
        response = client.get('/')
        assert response.status_code == 200

    # def test_should_return_hello_world(self, client):
    #     response = client.get('/index')
    #     data = response.data.decode() #Permet de décoder la data dans la requête
    #     assert data == 'Hello, World!'

    def test_login(self, client):
        email = 'testEmail'
        password = 'testPassword'
        headers = {'Content-Type': 'application/json'}
        response = client.post('/api/login', headers=headers, data={'email' : email, 'password' : password})
        pprint(response.data)
        assert response.status_code == 200
