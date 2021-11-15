from fastapi import FastAPI
from libs.dictionary import rest_molog
from libs.data_forms import SKU_form

app = FastAPI()
api = rest_molog()

@app.get("/")
def read_root():
    return {"API": "Molog_WMS"}


@app.get("/sku/{auth}")
def create_and_update_SKU(auth: str):
    if auth == 'S@NKO_CR@ATE':
        data = SKU_form()
        res = api.create_and_update_SKU()

    return {'create_sku':'you are not access'}