from flask_restful import Resource
from flask import request
from modules.config_generator import config_generator
import requests

location = config_generator.locations
search_url = config_generator.find_endpoint


class SearchStoreResource(Resource):
    def post(self):
        content = request.get_json(silent=True)
        if content['location'] not in location:
            return {'code': 401, 'msg': 'Invalid location name'}
        if len(content['name']) < 2:
            return {'code': 400, 'msg': 'Too short search object'}

        params = {'name': content['name'], 'location': location[content['location']]}
        response = requests.post(search_url, params=params)
        return response.json()
