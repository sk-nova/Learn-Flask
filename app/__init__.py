from flask import Flask


def create_app() -> Flask:

    app = Flask(__name__)

    from app.routes import root_bp

    app.register_blueprint(root_bp)

    return app
