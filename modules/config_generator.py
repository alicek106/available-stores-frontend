import boto3
import os
import json


class ConfigGenerator:
    def __init__(self):
        self.locations = {
            '수원': 1,
            '용인': 2,
            '고양': 3
        }

        if os.environ['local'] == '1':
            client = boto3.client('ssm', region_name='ap-northeast-2')
        elif os.environ['local'] == '0':
            client = boto3.client('ssm', region_name='ap-northeast-2', endpoint_url=os.environ['ssm_url'])

        params = client.get_parameter(
            Name='api_gateway_url',
            WithDecryption=True
        )
        self.find_endpoint = params['Parameter']['Value'] + 'find_available_stores'
        self.send_endpoint = params['Parameter']['Value'] + 'send_message'

        with open('updates.json') as data_file:
            self.updates = json.load(data_file)


config_generator = ConfigGenerator()
