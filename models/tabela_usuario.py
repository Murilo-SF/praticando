from praticando.extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    pedidos = db.relationship('Pedido', backref='usuarios', lazy=True)

    def to_dict(self):
        return {
            'id':self.id,
            'nome':self.nome,
            'email':self.email,
            'role':self.role
        }