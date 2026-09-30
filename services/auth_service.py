from praticando.schemas.schema_usuario import schema_usuario
from praticando.extensions import db
from praticando.models.tabela_usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from praticando.errors.exceptions import UsuarioJaExiste, UsuarioNaoEncontrado, SenhaIncorreta
from flask_jwt_extended import create_access_token

def service_registrar_usuario(data):
    data = schema_usuario.load(data)

    nome = data.get('nome')
    senha = data.get('senha')
    role = data.get('role')
    email = data.get('email')

    usuario_existente = Usuario.query.filter_by(nome=nome).first()

    if usuario_existente:
        raise UsuarioJaExiste()

    novo_usuario = Usuario(nome=nome, senha=generate_password_hash(senha), role=role, email=email)

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"message":"Usuário cadastrado com sucesso!"}), 201

def service_login_usuario(data):
    data = schema_usuario.load(data)

    nome = data.get('nome')
    senha = data.get('senha')

    usuario_existente = Usuario.query.filter_by(nome=nome).first()

    if not usuario_existente:
        raise UsuarioNaoEncontrado()

    if not check_password_hash(usuario_existente.senha, senha):
        raise SenhaIncorreta()

    token = create_access_token(identity=str(usuario_existente.id), additional_claims={'nome':usuario_existente.nome, 'email':usuario_existente.email, 'role':usuario_existente.role})

    return jsonify ({'token':token}), 201