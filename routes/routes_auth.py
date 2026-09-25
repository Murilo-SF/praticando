from flask import Blueprint, jsonify, request
from praticando.services.auth_service import *

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/registrar', methods=['POST'])
def register_user():
    data = request.get_json()
    return service_register_user(data)