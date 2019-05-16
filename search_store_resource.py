from flask_restful import Resource
from flask import request
import requests

class SearchStoreResource(Resource):
    location = ['수원']
    search_url = 'https://irhracf5hi.execute-api.ap-northeast-2.amazonaws.com/default/FindAvailableStores'

    def post(self):
        content = request.get_json(silent=True)
        if content['location'] not in self.location:
            return {'code': 401, 'msg': 'Invalid location name'}
        if len(content['name']) < 2:
            return {'code': 400, 'msg': 'Too short search object'}

        params = {'name': content['name'], 'location': content['location']}
        response = requests.get(self.search_url, params=params)
        return response.json()
