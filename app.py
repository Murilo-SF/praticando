from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

#------------------------------------------------------ROUTES--------------------------------------------------------
from praticando.routes.routes_auth import auth_bp
from praticando.routes.routes_usuario import usuario_bp
from praticando.routes.routes_pedidos import pedidos_bp

#------------------------------------------------------CONFIG--------------------------------------------------------
from praticando.config import configs

#------------------------------------------------------DATABASE------------------------------------------------------
from praticando.extensions import db

#------------------------------------------------------ERRORS--------------------------------------------------------
from praticando.errors.handlers import register_errors

jwt = JWTManager()

def create_app(config="DevelopmentConfig"):
    
    app = Flask(__name__)

    app.config.from_object(configs[config])

    db.init_app(app)

    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(pedidos_bp)

    register_errors(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)