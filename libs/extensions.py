from datetime import datetime
import json

def check_expiration():

    ac_expired = False
    rf__expired = False

    path_create = 'resources/create_token.json'
    path_refresh = 'resources/refresh_token.json'

    now = datetime.now().date()

    file_create1 = open(path_create, 'r')
    data1 = json.loads(file_create1.read())

    # milisec to sec
    ate_sec_timestamp = data1['ACCESS_TOKEN_EXPIRE']/1000
    ac_token_expiration_date = datetime.fromtimestamp(ate_sec_timestamp).date()

    if ac_token_expiration_date <= now:
        ac_expired = True

        file_create2 = open(path_refresh, 'r')
        data2 = json.loads(file_create2.read())

        # milisec to sec
        rfe_sec_timestamp = data2['REFRESH_TOKEN_EXPIRE']/1000
        rf_token_expiration_date = datetime.fromtimestamp(rfe_sec_timestamp).date()

        if rf_token_expiration_date <= now:
            rf__expired = True

    return ac_expired, rf__expired


