from libs.data_forms import create_or_Update_SKU
from libs.settings import OPEN_URL, OPEN_APP_KEY, OPEN_SECRET_KEY, MOLOG_USERNAME, MOLOG_PASSWORD, \
                    PATH_REFRESH, PATH_CREATE
from libs.autogen import gen_timestamp, gen_signature
from libs.extensions import check_expiration, read_token
import requests
import json

def gen_token():
    api = rest_molog()
    ac_expired, rf_expired = check_expiration()

    if rf_expired == True:
        res1 = api.create_token()
        with open('resources/create_token.json', 'w') as f:
            json.dump(res1, f)

        res2 = api.refresh_token()
        with open('resources/refresh_token.json', 'w') as f:
            json.dump(res2, f)

    if ac_expired == True:
        res3 = api.refresh_token()
        with open('resources/refresh_token.json', 'w') as f:
            json.dump(res3, f)

    data = read_token('refresh')
    ACCESS_KEY = data['ACCESS_TOKEN']
    REFRESH_TOKEN = data['REFRESH_TOKEN']
    
    return ACCESS_KEY, REFRESH_TOKEN


class rest_molog(object):

    def __init__(self):

        ACCESS_KEY, REFRESH_TOKEN = gen_token()

        self.url = OPEN_URL
        self.app_key = OPEN_APP_KEY
        self.secret_key = OPEN_SECRET_KEY
        self.username = MOLOG_USERNAME
        self.password = MOLOG_PASSWORD
        self.timestamp = str(gen_timestamp())
        self.access_key = ACCESS_KEY
        self.refresh_key = REFRESH_TOKEN


    def gen_details_default(self, types):

        url = ''
        
        if types == "create_token":
            sign = gen_signature(types)
            url = self.url+"/system/token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign
        if types == "delete_token":
            # use the same path as 'create_token'
            sign = gen_signature("create_token")
            url = self.url+"/system/token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+self.access_key
            print(url)
        if types == "refresh_token":
            sign = gen_signature(types)
            url = self.url+"/system/refresh_token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign
        # if types == "create_SKU":
        #     sign = gen_signature(types)
        #     url = self.url+"/sku/sku?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+access_key
        # if types == "update_SKU_BOM":
        #     sign = gen_signature(types)
        #     url = self.url+"/sku/skubom?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+access_key
        # if types == "create_PSO":
        #     url = self.url+"/pso/pso?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+access_key
        # if types == "create_update_partner":
        #     url = self.url+"/partner/partner?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+access_key
        # if types == "get_inventory":
        #     url = self.url+"/inventory/list?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+access_key

        ID = {
            'USERNAME' : self.username,
            'PASSWORD' : self.password
        }
        
        payload = json.dumps(ID)

        headers = {
            'Content-Type' : 'application/json'
        }
 
        return url, payload, headers
    
    def create_token(self):

        url, payload, headers = self.gen_details_default("create_token", '')
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    def delete_token(self):

        url, payload, headers = self.gen_details_default("delete_token", '')
        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    def refresh_token(self):

        url, __, headers = self.gen_details_default("refresh_token", '')
        re_token = {"REFRESH_TOKEN" : self.refresh_key }

        payload = json.dumps(re_token)
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    def create_SKU(self):

        url, __, headers = self.gen_details_default("create_SKU", '')
        payload = create_or_Update_SKU()
        response = requests.request("POST", url, headers=headers, data=payload)


        print(response.text)
        return response.json()
