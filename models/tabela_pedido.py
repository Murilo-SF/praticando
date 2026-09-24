from praticando.extensions import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False)