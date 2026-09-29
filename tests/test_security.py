def test_register_user(client):

    response = client.post(
        "/auth/register",
        json={
            "name": "Test User",
            "email": "pytest@gmail.com",
            "password": "password123"
        }
    )


    assert response.status_code in [200, 400]



def test_login_user(client):

    response = client.post(
        "/auth/login",
        json={
            "email": "vardhan@gmail.com",
            "password": "admin123"
        }
    )


    assert response.status_code == 200


    data = response.json()


    assert data["success"] is True

    assert "access_token" in data["data"]