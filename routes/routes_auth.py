from flask import Blueprint, jsonify, request
from praticando.services.auth_service import *

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/registrar', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    return service_registrar_usuario(data)

@auth_bp.route('/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    return service_login_usuario(data)