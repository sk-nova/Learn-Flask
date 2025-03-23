from app import create_app
from app.config import DevelopmentConfig


flask_app = create_app(config_class=DevelopmentConfig)
