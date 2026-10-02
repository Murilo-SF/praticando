from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from praticando.schemas.schema_pedido import schema_pedido
from praticando.services.pedido_service import *
from praticando.decorators.auth_decorator import role_required

pedidos_bp = Blueprint('pedidos_bp', __name__, url_prefix='/pedido')

@pedidos_bp.route('/registrar', methods=['POST'])
@jwt_required()
def registrar_meu_pedido():
    id = get_jwt_identity()
    data = schema_pedido.load(request.get_json())
    return service_registrar_meu_pedido(data, id)

@pedidos_bp.route('/registrar/<int:id>', methods=['POST'])
@role_required('admin')
def registrar_pedido_admin(id):
    data = schema_pedido.load(request.get_json())
    return service_registrar_pedido_admin(data, id)

@pedidos_bp.route('/meus', methods=['GET'])
@jwt_required()
def buscar_meus_pedidos():
    id = get_jwt_identity()
    return service_buscar_meus_pedidos(id)

@pedidos_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def buscar_pedidos_admin(id):
    return service_buscar_meus_pedidos(id)

@pedidos_bp.route('/atualizar/<int:pedido_id>', methods=['PUT'])
@role_required('admin')
def atualizar_pedido(pedido_id):
    data = schema_pedido.load(request.get_json())
    return service_atualizar_pedido(data, pedido_id)

@pedidos_bp.route('/deletar/<int:pedido_id>', methods=['DELETE'])
@role_required('admin')
def deletar_pedido(pedido_id):
    data = request.get_json()
    cliente_id = data.get('cliente_id')
    return service_deletar_pedido(cliente_id, pedido_id)