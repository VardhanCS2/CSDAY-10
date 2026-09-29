def test_create_order(client, auth_headers):

    response = client.post(
        "/orders/",
        headers=auth_headers
    )


    assert response.status_code == 200



def test_get_orders(client, auth_headers):

    response = client.get(
        "/orders/",
        headers=auth_headers
    )


    assert response.status_code == 200