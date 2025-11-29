# src/flask_simple_api/__init__.py
from flask import Flask
from src.flask_simple_api.home.routes import home_bp
# from src.flask_simple_api.api.routes import api_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    # app.register_blueprint(api_bp)
    return app
