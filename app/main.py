from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"FastAPI": "Molog_WMS"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}