from flask import Flask
from app.extensions import *


def create_app(config_class=None) -> Flask:
    """
    Create and configure an instance of the Flask application.
    Args:
        config_class (optional): The configuration class to use for the application.
                                 If None, the default configuration will be used.
    Returns:
        Flask: The configured Flask application instance.
    """

    # Create a Flask instance
    app = Flask(__name__)

    # Load Configurations
    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_object("app.config.Config")

    # Bind the app with Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app import models

    # Import and Register blueprints
    from app.routes import root_bp

    app.register_blueprint(root_bp)

    # Return Flask instance
    return app
