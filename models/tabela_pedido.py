from praticando.extensions import db

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'pedido_id':self.id,
            'cliente_id':self.cliente_id,
            'valor':self.valor
        }