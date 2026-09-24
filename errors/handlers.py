from praticando.errors.exceptions import UsuarioNaoEncontrado, PedidoNaoEncontrado, SenhaIncorreta
from flask import jsonify

def register_errors(app):
    @app.errorhandler(UsuarioNaoEncontrado)
    def usuario_nao_encontrado():
        return jsonify({"error":"Usuário não encontrado!"}), 404
    
    @app.errorhandler(PedidoNaoEncontrado)
    def pedido_nao_encontrado():
        return jsonify({"error":"Pedido não encontrado!"}), 404
    
    @app.errorhandler(SenhaIncorreta)
    def senha_incorreta():
        return jsonify({"error":"Senha Incorreta!"}), 400
    