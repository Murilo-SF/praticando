import pytest

def test_login(client):
    response = client.post('/auth/login', json={"nome":"Mauro Betin","senha":"123456"})
    assert response.status_code == 201
    assert "token" in response.get_json()

def test_login_name_and_password_min(client):
    response = client.post('/auth/login', json={"nome":"Mau", "senha":"12345"})
    assert response.status_code == 400
    assert "error" in response.get_json()
    assert response.get_json()["error"]["nome"][0] == "Shorter than minimum length 4."
    assert response.get_json()["error"]["senha"][0] == "Shorter than minimum length 6."

def test_login_user_not_found(client):
    response = client.post('/auth/login', json={"nome":"DeBruyne", "senha":"123456"})
    assert "error" in response.get_json()
    assert response.status_code == 404
    assert response.get_json()["error"] == "Usuário não encontrado!"

def test_login_incorrect_password(client):
    response = client.post('/auth/login', json={"nome":"Mauro Betin", "senha":"654321"})
    assert response.status_code == 401
    assert "error" in response.get_json()
    assert response.get_json()["error"] == "Senha Incorreta!"