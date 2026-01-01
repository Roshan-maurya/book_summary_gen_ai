from flask import Flask
from app.config.config import Config
from app.extensions.db import db
from app.extensions.jwt import jwt
from app.routes.book_routes import book_bp
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(book_bp)

    return app
