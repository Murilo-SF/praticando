import pytest

def test_register_order(client, user, header_admin):
    response = client.post('/pedido/registrar', json={"cliente_id":user.id, "valor":100}, headers=header_admin)
    assert response.status_code == 201
    assert "message" in response.get_json()
    assert response.get_json()["message"] == "Pedido registrado com sucesso!"

def test_get_my_orders(client, header_user):
    response = client.get('/pedido/meus', headers=header_user)
    assert response.status_code == 200
    assert "pedidos" in response.get_json()

def test_get_orders_by_id(client, user, header_admin):
    response = client.get(f'/pedido/{user.id}', headers=header_admin)
    assert response.status_code == 200
    assert "pedidos" in response.get_json()
    assert response.get_json()["pedidos"] == []

def test_get_orders_by_id_non_existent(client, header_admin):
    response = client.get('/pedido/9999999', headers=header_admin)
    assert response.status_code == 404
    assert "error" in response.get_json()
    assert response.get_json()["error"] == "Usuário não encontrado!"