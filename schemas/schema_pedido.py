from marshmallow import Schema, fields
from marshmallow.validate import Length

class SchemaPedido(Schema):
    cliente_id = fields.Int(required=True)
    valor = fields.Float(required=True)

schema_pedido = SchemaPedido()