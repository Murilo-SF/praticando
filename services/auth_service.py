from praticando.schemas.schema_usuario import schema_usuario
from praticando.extensions import db
from praticando.models.tabela_usuario import Usuario
from werkzeug.security import generate_password_hash
from flask import jsonify
from praticando.errors.exceptions import UsuarioJaExiste

def service_register_user(data):
    data = schema_usuario.load(data)

    nome = data.get('nome')
    senha = data.get('senha')
    role = data.get('role')
    email = data.get('email')

    existing_user = Usuario.query.filter_by(nome=nome).first()

    if existing_user:
        raise UsuarioJaExiste()

    novo_usuario = Usuario(nome=nome, senha=generate_password_hash(senha), role=role, email=email)

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"message":"User successfully registered!"})