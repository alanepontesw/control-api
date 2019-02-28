import json
from flask_restful import Resource, request
from interface.restful import APP, API
from domain.control_api import ControlAPI
from domain.request import Request
from config.control_api_config import ControlAPIConfig

class Product(Resource):

    @staticmethod
    def post():
        body = json.loads(request.get_data().decode())
        if ControlAPI().request_is_denied(Request(method=request.method, body=body)):
            return 403
        return 200

API.add_resource(Product, '/v1/products')

if __name__ == '__main__':
    APP.run(host=ControlAPIConfig.HOST)
    