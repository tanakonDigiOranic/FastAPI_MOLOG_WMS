from libs.settings import OPEN_URL, OPEN_APP_KEY, OPEN_SECRET_KEY, MOLOG_USERNAME, MOLOG_PASSWORD, PATH_CREATE, PATH_REFRESH
import datetime
import requests
import json
import hashlib
import hmac



def read_token(option):

    data = None
    pc = PATH_CREATE+".json"
    pr = PATH_REFRESH+".json"

    if option == 'read_refresh_in_create_token':
        file_create1 = open(pc, 'r')
        data = json.loads(file_create1.read())

    if option == 'read_access_in_refresh':
        file_create2 = open(pr, 'r')
        data = json.loads(file_create2.read())

    return data


def check_expiration():

    ac_expired = False
    rf__expired = False

    now = datetime.datetime.now().date()
    data1 = read_token('read_access_in_refresh')

    # milisec to sec
    ate_sec_timestamp = data1['ACCESS_TOKEN_EXPIRE']/1000
    ac_token_expiration_date = datetime.datetime.fromtimestamp(ate_sec_timestamp).date()
    print("expired :", ac_token_expiration_date, "-- now :", now)

    if ac_token_expiration_date <= now:
        ac_expired = True

        data2 = read_token('read_refresh_in_create_token')

        # milisec to sec
        rfe_sec_timestamp = data2['REFRESH_TOKEN_EXPIRE']/1000
        rf_token_expiration_date = datetime.datetime.fromtimestamp(rfe_sec_timestamp).date()

        if rf_token_expiration_date <= now:
            rf__expired = True

    return ac_expired, rf__expired

def gen_timestamp():
    # TimestampMillisec64
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)


def gen_signature(path):

    end_of_row = ('APP_KEY{}TIMESTAMP{}'.format(OPEN_APP_KEY,gen_timestamp()))

    if path == 'create_token':
        mes = bytes('/system/token{}'.format(end_of_row), 'utf-8')
    if path == "refresh_token":
        mes = bytes('/system/refresh_token{}'.format(end_of_row), 'utf-8')
    if path == "create_SKU":
        mes = bytes('/sku/sku{}'.format(end_of_row), 'utf-8')

    secret = bytes(OPEN_SECRET_KEY, 'utf-8')
    hash = hmac.new(secret, mes, hashlib.sha256)

    # to lowercase hexits
    SIGN = hash.hexdigest().upper()
    return SIGN

def back_up_token():
    
    backup_pc = PATH_CREATE+'_backup'+'.json'
    res2 = read_token('read_refresh_in_create_token')

    with open(backup_pc, 'w') as f:
        json.dump(res2, f)


class rest_molog_token(object):

    def __init__(self):

        data1 = read_token('read_access_in_refresh')
        data2 = read_token('read_refresh_in_create_token')

        self.url = OPEN_URL
        self.app_key = OPEN_APP_KEY
        self.secret_key = OPEN_SECRET_KEY
        self.username = MOLOG_USERNAME
        self.password = MOLOG_PASSWORD
        self.timestamp = str(gen_timestamp())
        self.access_key = data1['ACCESS_TOKEN']
        self.refresh_key = data2['REFRESH_TOKEN']


    def gen_details_default(self, types):

        url = ''
        
        if types == "create_token":
            sign = gen_signature(types)
            url = self.url+"/system/token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign
        if types == "delete_token":
            # use the same path as 'create_token'
            sign = gen_signature("create_token")
            url = self.url+"/system/token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign+"&ACCESS_TOKEN="+self.access_key
        if types == "refresh_token":
            sign = gen_signature(types)
            url = self.url+"/system/refresh_token?APP_KEY="+self.app_key+"&TIMESTAMP="+self.timestamp+"&SIGN="+sign


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

        url, payload, headers = self.gen_details_default("create_token")
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    def delete_token(self):

        url, payload, headers = self.gen_details_default("delete_token")
        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)
        return response.json()

    def refresh_token(self):

        url, __, headers = self.gen_details_default("refresh_token")
        re_token = {"REFRESH_TOKEN" : self.refresh_key }

        payload = json.dumps(re_token)
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        return response.json()
    
