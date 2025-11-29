# tests/test_factory.py
from src.flask_simple_api import create_app


def test_create_app():
    app = create_app()
    assert app is not None
