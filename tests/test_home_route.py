# tests/test_home_root.py

from src.flask_simple_api import create_app

def test_home_route():
    app = create_app()
    client = app.test_client()

    res = client.get("/")
    assert res.status_code == 200
