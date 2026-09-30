from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from praticando.services.usuario_service import *

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/usuario')

@usuario_bp.route('/eu', methods=['GET'])
@jwt_required()
def informacoes_usuario():
    id = get_jwt_identity()
    return service_buscar_meu_usuario(int(id))