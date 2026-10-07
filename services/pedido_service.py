from praticando.models.tabela_pedido import Pedido
from praticando.models.tabela_usuario import Usuario
from praticando.extensions import db
from praticando.errors.exceptions import *
from flask import jsonify

def service_registrar_meu_pedido(data, id):

    usuario = db.session.get(Usuario, id)

    if not usuario:
        raise UsuarioNaoEncontrado()

    valor = data.get('valor')

    novo_pedido = Pedido(cliente_id=id, valor=valor)

    db.session.add(novo_pedido)

    db.session.flush()

    return jsonify ({"message": "Pedido registrado com sucesso!","pedido":novo_pedido.to_dict()}), 201

def service_registrar_pedido_admin(data, id):

    usuario = db.session.get(Usuario, id)

    if not usuario:
        raise UsuarioNaoEncontrado()

    valor = data.get('valor')

    novo_pedido = Pedido(cliente_id=id, valor=valor)

    db.session.add(novo_pedido)

    db.session.flush()

    return jsonify({"message":"Pedido registrado com sucesso!", "pedido":novo_pedido.to_dict()}), 201

def service_buscar_meus_pedidos(id):

    usuario = db.session.get(Usuario, id)

    if not usuario:
        raise UsuarioNaoEncontrado()

    pedidos = usuario.pedidos

    return jsonify ({"pedidos":[pedido.to_dict() for pedido in pedidos]}), 200

def service_buscar_pedidos_admin(id):

    usuario = db.session.get(Usuario, id)

    if not usuario:
        raise UsuarioNaoEncontrado()

    pedidos = usuario.pedidos

    return jsonify ({"pedidos":[pedido.to_dict() for pedido in pedidos]}), 200

def service_atualizar_pedido(data, pedido_id):

    usuario = db.session.get(Usuario, data.get('cliente_id'))

    pedido = db.session.get(Pedido, pedido_id)

    if not usuario:
        raise UsuarioNaoEncontrado()

    if not pedido:
        raise PedidoNaoEncontrado()

    valor = data.get('valor')
    cliente_id = data.get('cliente_id')

    pedido.cliente_id = cliente_id
    pedido.valor = valor

    db.session.flush()

    return jsonify ({"message": "Pedido atualizado com sucesso!","pedido":pedido.to_dict()}), 200

def service_deletar_pedido(cliente_id, pedido_id):

    usuario = db.session.get(Usuario, cliente_id)

    pedido = db.session.get(Pedido, pedido_id)

    if not pedido:
        raise PedidoNaoEncontrado()

    if not usuario:
        raise UsuarioNaoEncontrado()

    db.session.delete(pedido)
    db.session.flush()

    return jsonify ({"message":"Pedido deletado com sucesso!"}), 200