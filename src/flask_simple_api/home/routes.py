# src/flask_simple_api/home/routes.py

from flask import Blueprint
from textwrap import dedent

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def index():
    html = dedent("""\
        <div style="
            min-height: 95vh;
            min-width: 95vw;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 1.2rem;
        ">
            <h1 style="user-select: none;">Welcome to Flask Home.</h1>

            <div style="
                display: flex;
                flex-direction: row;
                gap: 1.2rem;
            ">
                <a href="/hello-json" target="_blank"
                   style="
                       padding: 0.6rem 1.2rem;
                       border: 1px solid #ccc;
                       text-decoration: none;
                       color: #333;
                       background: #f7f7f7;
                       width: 150px;
                       text-align: center;
                       pointer-events: none;
                       user-select: none;
                   ">
                    <span>Hello-Json</span>
                    <br>
                    <span>（無効）</span>
                </a>

                <a href="/time-json" target="_blank"
                   style="
                       padding: 0.6rem 1.2rem;
                       border: 1px solid #ccc;
                       text-decoration: none;
                       color: #333;
                       background: #f7f7f7;
                       width: 150px;
                       text-align: center;
                       pointer-events: none;
                       user-select: none;
                   ">
                    <span>Time-Json</span>
                    <br>
                    <span>（無効）</span>
                </a>
            </div>
        </div>
    """)
    return html
