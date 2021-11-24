from libs.settings import OPEN_URL, OPEN_APP_KEY, OPEN_SECRET_KEY, MOLOG_USERNAME, MOLOG_PASSWORD
from libs.autogen import gen_signature, gen_timestamp, read_token
from libs.mologutils import gen_token
import requests
import json

# auto refresh token
gen_token()

class rest_molog(object):

    def __init__(self):

        data = read_token('read_access_in_refresh')

        self.url = OPEN_URL
        self.app_key = OPEN_APP_KEY
        self.secret_key = OPEN_SECRET_KEY
        self.username = MOLOG_USERNAME
        self.password = MOLOG_PASSWORD
        self.timestamp = str(gen_timestamp())
        self.access_key = data['ACCESS_TOKEN']



    def gen_details_default(self, types):

        url = ''
        
        if types == "create_SKU":
            sign = gen_signature(types)
            url = self.url+"/sku/sku?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+self.access_key
        # if types == "update_SKU_BOM":
        #     sign = gen_signature(types)
        #     url = self.url+"/sku/skubom?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+self.access_key
        # if types == "create_PSO":
        #     url = self.url+"/pso/pso?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+self.access_key
        # if types == "create_update_partner":
        #     url = self.url+"/partner/partner?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+self.access_key
        # if types == "get_inventory":
        #     url = self.url+"/inventory/list?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+self.access_key

        ID = {
            'USERNAME' : self.username,
            'PASSWORD' : self.password
        }
        
        payload = json.dumps(ID)

        headers = {
            'Content-Type' : 'application/json'
        }
 
        return url, payload, headers
    
    
    #create and update
    def create_SKU(self, payload):

        url, __, headers = self.gen_details_default("create_SKU")
        response = requests.request("POST", url, headers=headers, data=payload)


        print(response.text)
        return response.json()
