from libs.autogen import rest_molog_token, check_expiration, read_token, back_up_token
from libs.settings import PATH_CREATE, PATH_REFRESH
import json


def gen_token():
    api = rest_molog_token()
    ac_expired, rf_expired = check_expiration()
    is_not_error = read_token('read_refresh_in_create_token')
    if is_not_error["ACCESS_TOKEN"]:
        back_up_token()

    pc = PATH_CREATE+".json"
    pr = PATH_REFRESH+".json"

    if rf_expired == True:
        res1 = api.create_token()
        
        with open(pc, 'w') as f:
            json.dump(res1, f)

        res2 = api.refresh_token()
        with open(pr, 'w') as f:
            json.dump(res2, f)

    if ac_expired == True:
        res3 = api.refresh_token()
        with open(pr, 'w') as f:
            json.dump(res3, f)