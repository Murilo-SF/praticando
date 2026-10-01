from flask import jsonify
from praticando.extensions import db
from praticando.models.tabela_usuario import Usuario
from praticando.errors.exceptions import UsuarioNaoEncontrado

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