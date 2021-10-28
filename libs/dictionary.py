from libs.settings import OPEN_URL, OPEN_APP_KEY, OPEN_SECRET_KEY, OPEN_ACCESS_KEY, USERNAME, PASSWORD, TIMESTAMP, SIGN
import requests

def create_token():

    url = OPEN_URL+"/system/token?APP_KEY="+OPEN_APP_KEY+"&TIMESTAMP="+TIMESTAMP+"&SIGN="+SIGN

    payload = {
        'USERNAME' : USERNAME,
        'PASSWORD' : PASSWORD,
    }

    headers = {
        'Content-Type' : 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
