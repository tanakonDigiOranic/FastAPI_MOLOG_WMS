from libs.settings import PATH_CREATE, PATH_REFRESH
from datetime import datetime
import json


def read_token(option):

    data = None

    if option == 'create':
        file_create1 = open(PATH_CREATE, 'r')
        data = json.loads(file_create1.read())

    if option == 'refresh':
        file_create2 = open(PATH_REFRESH, 'r')
        data = json.loads(file_create2.read())

    return data

def check_expiration():

    ac_expired = False
    rf__expired = False

    now = datetime.now().date()
    data1 = read_token('create')

    # milisec to sec
    ate_sec_timestamp = data1['ACCESS_TOKEN_EXPIRE']/1000
    ac_token_expiration_date = datetime.fromtimestamp(ate_sec_timestamp).date()

    if ac_token_expiration_date <= now:
        ac_expired = True

        data2 = read_token('create')

        # milisec to sec
        rfe_sec_timestamp = data2['REFRESH_TOKEN_EXPIRE']/1000
        rf_token_expiration_date = datetime.fromtimestamp(rfe_sec_timestamp).date()

        if rf_token_expiration_date <= now:
            rf__expired = True

    return ac_expired, rf__expired


