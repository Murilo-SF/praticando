import pytest

def test_get_my_user(client, header_admin):
    response = client.get('/usuario/eu', headers=header_admin)
    assert response.status_code == 200
    assert "usuario" in response.get_json()

def test_get_all_users(client, header_admin):
    response = client.get('/usuario/todos', headers=header_admin)
    assert response.status_code == 200
    assert "usuarios" in response.get_json()

def test_get_all_users_without_admin(client, header_user):
    response = client.get('/usuario/todos', headers=header_user)
    assert response.status_code == 403
    assert "error" in response.get_json()
    assert response.get_json()["error"] == "Acesso negado!"

def test_route_admin_without_admin(client, header_user):
    response = client.get('/usuario/admin', headers=header_user)
    assert response.status_code == 403
    assert "error" in response.get_json()
    assert response.get_json()["error"] == "Acesso negado!"

def test_get_user_by_id_with_admin(client, header_admin):
    response = client.get('/usuario/1', headers=header_admin)
    assert response.status_code == 200
    assert "usuario" in response.get_json()

def test_get_user_by_id_without_admin(client, header_user):
    response = client.get('/usuario/1', headers=header_user)
    assert response.status_code == 403
    assert "error" in response.get_json()
    assert response.get_json()["error"] == "Acesso negado!"

def test_update_user(client, admin, header_admin):
    response = client.put(f'/usuario/atualizar/{admin.id}', json={"nome":"Admin Testee", "senha":"123456"}, headers=header_admin)
    assert response.status_code == 200
    assert "message" in response.get_json()
    assert response.get_json()["message"] == "Usuário atualizado com sucesso!"

def test_update_user_without_admin(client, admin, header_user):
    response = client.put(f'/usuario/atualizar/{admin.id}', json={"nome":"Admin Teste", "senha":"123456"}, headers=header_user)
    assert response.status_code == 403
    assert "error" in response.get_json()
    assert response.get_json()["error"] == "Acesso negado!"

def test_delete_user(client, user, header_admin):
    response = client.delete(f'/usuario/deletar/{user.id}', headers=header_admin)
    assert response.status_code == 200
    assert "message" in response.get_json()
    assert response.get_json()["message"] == "Usuário deletado com sucesso!"

def test_delete_user_without_admin(client, user, header_user):
    response = client.delete(f'/usuario/deletar/{user.id}', headers=header_user)
    assert response.status_code == 403
    assert "error" in response.get_json()
    assert response.get_json()["error"] == "Acesso negado!"