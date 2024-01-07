from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}})

    from .api import weather

    app.register_blueprint(weather.bp)

    return app