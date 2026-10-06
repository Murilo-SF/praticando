import pytest
from praticando.extensions import db
from praticando.app import create_app
from praticando.models.tabela_usuario import Usuario
from werkzeug.security import generate_password_hash

@pytest.fixture(scope="session")
def app():
    app = create_app("TestingConfig")
    with app.app_context():
        yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def session(app):
    db_session = db.session()
    yield db_session
    db_session.rollback()

@pytest.fixture()
def admin(session):
    admin_user = Usuario(nome="Admin User", senha=generate_password_hash("123456"), role="admin", email="NULL")
    session.add(admin_user)
    session.flush()
    return admin_user

@pytest.fixture()
def token_admin(admin, client):
    response = client.post('/auth/login', json={"nome":"Admin User","senha":"123456"})
    token = response.get_json()["token"]
    return token

@pytest.fixture()
def header_admin(token_admin):
    headers_admin = {"Authorization":f"Bearer {token_admin}"}
    return headers_admin

@pytest.fixture()
def user(session):
    new_user = Usuario(nome="Usuário Comum", senha=generate_password_hash("123456"), role="user", email="NULL")
    session.add(new_user)
    session.flush()
    return new_user

@pytest.fixture()
def token_user(user, client):
    response = client.post('/auth/login', json={"nome":user.nome, "senha":"123456"})
    token = response.get_json()["token"]
    return token

@pytest.fixture()
def header_user(token_user):
    headers_user = {"Authorization":f"Bearer {token_user}"}
    return headers_user