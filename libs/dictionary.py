from libs.settings import OPEN_URL, OPEN_APP_KEY, OPEN_SECRET_KEY, MOLOG_USERNAME, MOLOG_PASSWORD, REFRESH_TOKEN
from libs.autogen import gen_timestamp, gen_signature
from libs.data_forms import SKU_form  
import requests
import json


class rest_molog(object):

    def __init__(self):
        self.url = OPEN_URL
        self.app_key = OPEN_APP_KEY
        self.secret_key = OPEN_SECRET_KEY
        self.username = MOLOG_USERNAME
        self.password = MOLOG_PASSWORD
        self.timestamp = str(gen_timestamp())


    def gen_details_default(self, types, access_key):


        url = ''
        
        if types == "create_token":
            sign = gen_signature(types)
            url = self.url+"/system/token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign
        if types == "refresh_token":
            sign = gen_signature(types)
            url = self.url+"/system/refresh_token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign
        if types == "create_and_update_SKU":
            sign = gen_signature(types)
            url = self.url+"/sku/sku?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+access_key
        # if types == "update_SKU_BOM":
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

    def refresh_token(self):

        url, __, headers = self.gen_details_default("refresh_token", '')
        re_token = {"REFRESH_TOKEN" : REFRESH_TOKEN }

        payload = json.dumps(re_token)
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    def create_and_update_SKU(self):

        url, __, headers = self.gen_details_default("create_and_update_SKU", '')
        payload = SKU_form()
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
