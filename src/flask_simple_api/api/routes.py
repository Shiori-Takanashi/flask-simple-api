from flask import Blueprint, jsonify
from .hello import get_hello
from .time import get_time

api_bp = Blueprint("api", __name__)


@api_bp.route("/hello-json")
def hello_page():
    return jsonify(get_hello())


@api_bp.route("/time-json")
def time_page():
    return jsonify(get_time())
