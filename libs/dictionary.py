from libs.settings import OPEN_URL, OPEN_APP_KEY, OPEN_SECRET_KEY, OPEN_ACCESS_KEY, MOLOG_USERNAME, MOLOG_PASSWORD, TIMESTAMP, API_CODE
import requests
import json



class rest_molog(object):

    def __init__(self):
        self.url = OPEN_URL
        self.app_key = OPEN_APP_KEY
        self.secret_key = OPEN_SECRET_KEY
        self.access_key = OPEN_ACCESS_KEY
        self.username = MOLOG_USERNAME
        self.password = MOLOG_PASSWORD
        self.timestamp = TIMESTAMP
        self.sign = API_CODE

    def gen_details_default(self, types):

        # if types == "create_token":
        #     url = self.url+"/system/token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+self.sign
        # if types == "refresh_token":
        #     url = self.url+"/system/refresh_token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+self.sign
        if types == "create_and_update_SKU":
            url = self.url+"/sku/sku?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+self.sign+"&ACCESS_TOKEN="+self.access_key
        if types == "update_SKU_BOM":
            url = self.url+"/sku/skubom?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+self.sign+"&ACCESS_TOKEN="+self.access_key
        if types == "create_PSO":
            url = self.url+"/pso/pso?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+self.sign+"&ACCESS_TOKEN="+self.access_key
        if types == "create_update_partner":
            url = self.url+"/partner/partner?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+self.sign+"&ACCESS_TOKEN="+self.access_key
        if types == "get_inventory":
            url = self.url+"/inventory/list?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+self.sign+"&ACCESS_TOKEN="+self.access_key

        ID = {
            'USERNAME' : self.username,
            'PASSWORD' : self.password
        }
        
        payload = json.dump(ID)

        headers = {
            'Content-Type' : 'application/json'
        }
 
        return url, payload, headers
    
    # def create_token(self):

    #     url, payload, headers = self.gen_details_default("create_token")
    #     response = requests.request("POST", url, headers=headers, data=payload)

    #     print(response.text)

    # def refresh_token(self):
        
    #     url, __, headers = self.gen_details_default("refresh_token")
    #     re_token = {
    #         "REFRESH_TOKEN" : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMSIsImN1c3RfaWQiOjQsImFwaV9zaWduYXR1cmUiOiJjR1NKNmUzVlI1RiV5a3NmcjR4a082M1BXUFhEODlIS0w1R285NTVsSEUjUlFOQzF4VEtnUXduSktkNnFsNyUlIiwiaWF0IjoxNjA1MDgwODU2LCJleHAiOjE2MDc2NzI4NTZ9.J6G7Af5yeM-uJ5JNwNJJZ85fhL_rJ5nJVYs1JupjnsM',
    #     }

    #     payload = json.dumps(re_token)
    #     response = requests.request("POST", url, headers=headers, data=payload)

    #     print(response.text)
    
    def create_and_update_SKU(self):

        url, payload, headers = self.gen_details_default("create_and_update_SKU")
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def update_SKU_BOM(self):
        
        url, payload, headers = self.gen_details_default("update_SKU_BOM")
        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)

    def create_PSO(self):
        
        url, payload, headers = self.gen_details_default("create_PSO")
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def create_update_partner(self):
        
        url, payload, headers = self.gen_details_default("create_update_partner")
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def get_inventory(self):

        page = "&PAGE="+1
        size = "&SIZE="+10
        date_from = "&RECEIVED_DATE_FROM="+"2019-11-16T00:00:00%2B07:00&"
        date_to = "&RECEIVED_DATE_TO="+"2020-11-16T23:59:59%2B07:00"
        sku_code = "&SKU_CODE="+"P97560204695"
        on_hand_only = "&ON_HAND_ONLY="+"true"
                
        url, payload, headers = self.gen_details_default("create_update_partner")

        urls = url+page+size+date_from+date_to+sku_code+on_hand_only
                
        payload = ""
        headers = {}

        response = requests.request("GET", urls, headers=headers, data=payload)

        print(response.text)