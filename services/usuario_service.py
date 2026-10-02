from flask import jsonify
from praticando.extensions import db
from praticando.models.tabela_usuario import Usuario
from praticando.errors.exceptions import UsuarioNaoEncontrado
from werkzeug.security import generate_password_hash

def service_buscar_meu_usuario(id):
    
        usuario = Usuario.query.filter_by(id=id).first()
    
        if not usuario:
            raise UsuarioNaoEncontrado()
    
        return jsonify ({"usuario":[usuario.to_dict()]}), 200

def service_admin():
      return jsonify({"message": "Bem-vindo Administrador!"}), 200

def service_buscar_todos_usuarios():

      usuarios = Usuario.query.all()

      return jsonify ({"usuarios": [usuario.to_dict() for usuario in usuarios]}), 200

def service_buscar_usuario_id(id):

      usuario = db.session.get(Usuario, id)

      if not usuario:
            raise UsuarioNaoEncontrado()

      return jsonify({"usuario": usuario.to_dict()}), 200

def service_atualizar_usuario(data, id):

      usuario = db.session.get(Usuario, id)

      if not usuario:
            raise UsuarioNaoEncontrado()

      nome = data.get('nome', usuario.nome)
      senha = data.get('senha', usuario.senha)
      role = data.get('role', usuario.role)
      email = data.get('email', usuario.email)

      usuario.nome = nome
      usuario.senha = generate_password_hash(senha)
      usuario.role = role
      usuario.email = email

      db.session.commit()

      return jsonify ({"message": "Usuário atualizado com sucesso!", "usuario": usuario.to_dict()}), 200

def service_deletar_usuario(id):

      usuario = db.session.get(Usuario, id)

      if not usuario:
            raise UsuarioNaoEncontrado()

      db.session.delete(usuario)
      db.session.commit()

      return jsonify({"message":"Usuário deletado com sucesso!"}), 200