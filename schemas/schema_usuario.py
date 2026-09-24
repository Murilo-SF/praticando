from marshmallow import Schema, fields
from marshmallow.validate import Length

class SchemaUsuario(Schema):
    nome = fields.Str(required=True, Length=min(4))
    senha = fields.Str(required=True, Length=min(6))
    email = fields.Str(required=True, Length=min(10))
    role = fields.Str(required=True, Length=min(4), load_default="user")

schema_usuario = SchemaUsuario()