from flask_restful import Resource
from flask import request
from modules.config_generator import config_generator
import requests

location = config_generator.locations
send_endpoint = config_generator.send_endpoint


class SendMessageResource(Resource):
    def put(self):
        content = request.get_json(silent=True)
        if len(content['message']) < 1:
            return {'code': 400, 'msg': 'Too short'}
        if len(content['message']) > 100:
            return {'code': 401, 'msg': 'Too long'}

        params = {'msg': content['message']}
        response = requests.post(send_endpoint, params=params)
        return response.json()
