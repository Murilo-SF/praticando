from praticando.errors.exceptions import *
from flask import jsonify
from marshmallow import ValidationError

def register_errors(app):
    @app.errorhandler(UsuarioNaoEncontrado)
    def usuario_nao_encontrado(error):
        return jsonify({"error":"Usuário não encontrado!"}), 404
    
    @app.errorhandler(PedidoNaoEncontrado)
    def pedido_nao_encontrado(error):
        return jsonify({"error":"Pedido não encontrado!"}), 404
    
    @app.errorhandler(SenhaIncorreta)
    def senha_incorreta(error):
        return jsonify({"error":"Senha Incorreta!"}), 400

    @app.errorhandler(ValidationError)
    def validation_error(error):
        return jsonify({"error":error.messages})

    @app.errorhandler(UsuarioJaExiste)
    def usuario_ja_existe(error):
        return jsonify({"error":"Usuário já existe!"}), 400

    @app.errorhandler(AcessoNegado)
    def usuario_ja_existe(error):
        return jsonify({"error":"Acesso negado!"}), 403