# src/flask_simple_api/__main__.py

from src.flask_simple_api import create_app


def main():
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == "__main__":
    main()
