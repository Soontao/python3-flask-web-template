from flask import Flask, request, jsonify
from flasgger import Swagger
from .api import mount_routes
from .config.swagger import swagger_config
from .error import set_error_handler

app = Flask(__name__)

app.config['SWAGGER'] = swagger_config

swagger = Swagger(app)

mount_routes(app)

set_error_handler(app)

if __name__ == "__main__":
    app.run()
