from flask import Flask, g
from flask_cors import CORS
from app_config import config
from flasgger import Swagger

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    CORS(app, expose_headers="token")

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    with app.app_context():
        g.setdefault("token", None)

    Swagger(app)

    return app