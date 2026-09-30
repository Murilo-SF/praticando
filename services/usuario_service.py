from flask import jsonify
from praticando.extensions import db
from praticando.models.tabela_usuario import Usuario
from praticando.errors.exceptions import UsuarioNaoEncontrado

def service_buscar_meu_usuario(id):
    
        usuario = Usuario.query.filter_by(id=id).first()
    
        if not usuario:
            raise UsuarioNaoEncontrado()
    
        return jsonify ({"usuario":[i.to_dict() for i in usuario]}), 200