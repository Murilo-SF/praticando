from flask import Blueprint, jsonify

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/teste')
def teste():
    return jsonify ({"Message": "Hello World!"})