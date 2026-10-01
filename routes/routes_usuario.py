from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from praticando.services.usuario_service import *
from praticando.decorators.auth_decorator import role_required

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/usuario')

@usuario_bp.route('/eu', methods=['GET'])
@jwt_required()
def informacoes_usuario():
    id = get_jwt_identity()
    return service_buscar_meu_usuario(int(id))

@usuario_bp.route('/admin')
@role_required("admin")
def admin():
    return service_admin()

@usuario_bp.route('/todos', methods=['GET'])
@role_required('admin')
def buscar_usuarios():
    return service_buscar_todos_usuarios()

@usuario_bp.route('/<int:id>', methods=['GET'])
@role_required('admin')
def buscar_usuario_id(id):
    return service_buscar_usuario_id(id)