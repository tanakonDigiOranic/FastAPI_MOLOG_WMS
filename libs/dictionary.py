from libs.settings import OPEN_URL, OPEN_APP_KEY, OPEN_SECRET_KEY, MOLOG_USERNAME, MOLOG_PASSWORD, REFRESH_TOKEN
from libs.autogen import gen_timestamp, gen_signature
from libs.data_forms import SKU_form 
from libs.extensions import check_expiration
import requests
import json

def gen_access_key():

    api = rest_molog()
    ac_expired, rf_expired = check_expiration()

    if ac_expired == True:
        res = api.refresh_token()
        with open('resources/refresh_token.json', 'w') as f:
            json.dump(res, f)




        
        

#     if option == 'create':

#         file_create = open('resources/create_token.json', 'r')
#         data = json.loads(file_create.read())

#         if data['ERROR_CODE']:
#             access_key_create = api.create_token()
#             with open('resources/create_token.json', 'w') as f:
#                 json.dump(access_key_create, f)
#             return access_key_create
        
#         elif data['ACCESS_KEY']:
#             return data['ACCESS_KEY']

#         else:
#             return data

#     if option == 'refresh':

#         file_create = open('resources/refresh_token.json', 'r')
#         data = json.loads(file_create.read())

#         if data['ERROR_CODE']:
#             access_key_refresh = api.refresh_token()
#             with open('resources/refresh_token.json', 'w') as f:
#                 json.dump(access_key_refresh, f)
#             return access_key_refresh

#         elif data['ACCESS_KEY']:
#             return data['ACCESS_KEY']

#         else:
#             return data



class rest_molog(object):

    def __init__(self):
        self.url = OPEN_URL
        self.app_key = OPEN_APP_KEY
        self.secret_key = OPEN_SECRET_KEY
        self.username = MOLOG_USERNAME
        self.password = MOLOG_PASSWORD
        self.timestamp = str(gen_timestamp())
        self.access_key = 1


    def gen_details_default(self, types, access_key):

        url = ''
        
        if types == "create_token":
            sign = gen_signature(types)
            url = self.url+"/system/token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign
        if types == "delete_token":
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
        re_token = {"REFRESH_TOKEN" : REFRESH_TOKEN }

        payload = json.dumps(re_token)
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
    def create_SKU(self):

        url, __, headers = self.gen_details_default("create_SKU", '')
        payload = SKU_form()
        response = requests.request("POST", url, headers=headers, data=payload)


        print(response.text)
        return response.json()
