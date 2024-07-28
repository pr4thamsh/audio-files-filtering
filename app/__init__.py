from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Import and register blueprints here
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app