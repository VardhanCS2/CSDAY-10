def test_add_cart(client, auth_headers):

    response = client.post(
        "/cart/add",
        headers=auth_headers,
        params={
            "product_identifier": "1",
            "quantity": 1
        }
    )


    assert response.status_code == 200



def test_get_cart(client, auth_headers):

    response = client.get(
        "/cart/",
        headers=auth_headers
    )


    assert response.status_code == 200