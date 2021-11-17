from libs.dictionary import rest_molog
import json
import os


def gen_access_key(option):

    api = rest_molog()

    if option == 'create':

        file_create = open('resources/create_token.json', 'r')
        data = json.loads(file_create.read())

        if data['ERROR_CODE']:
            access_key_create = api.create_token()
            with open('resources/create_token.json', 'w') as f:
                json.dump(access_key_create, f)
            return access_key_create
        
        elif data['ACCESS_KEY']:
            return data['ACCESS_KEY']

        else:
            return data

    if option == 'refresh':

        file_create = open('resources/refresh_token.json', 'r')
        data = json.loads(file_create.read())

        if data['ERROR_CODE']:
            access_key_refresh = api.refresh_token()
            with open('resources/refresh_token.json', 'w') as f:
                json.dump(access_key_refresh, f)
            return access_key_refresh

        elif data['ACCESS_KEY']:
            return data['ACCESS_KEY']

        else:
            return data

