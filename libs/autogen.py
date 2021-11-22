from libs.settings import OPEN_URL, OPEN_APP_KEY, OPEN_SECRET_KEY, MOLOG_USERNAME, MOLOG_PASSWORD
import hashlib
import hmac
import datetime

"""
timestamp & signature(path) auto generate every time.
timestamp >> millisec
signature >> using diffrent path

docs : https://app.mologtech.com/open-api-doc-th/
"""

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
