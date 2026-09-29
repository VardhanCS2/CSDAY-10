def test_get_products(client):

    response = client.get(
        "/products/"
    )


    assert response.status_code == 200


    data = response.json()


    assert data["success"] is True



def test_create_product(client, auth_headers):

    response = client.post(
        "/products/",
        headers=auth_headers,
        data={
            "name": "Test Product",
            "description": "Testing product",
            "price": "1000",
            "stock": "10"
        }
    )


    assert response.status_code == 200