from marshmallow import Schema, fields
from marshmallow.validate import Length

class SchemaUsuario(Schema):
    nome = fields.Str(required=True, validate=Length(4),)
    senha = fields.Str(required=True, validate=Length(6))
    email = fields.Str(validate=Length(10), default="NULL")
    role = fields.Str(validate=Length(4), default="user")

schema_usuario = SchemaUsuario()