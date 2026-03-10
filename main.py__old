from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, mundo!"}

@app.get("/itens/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return{"item_id": item_id, "q": q}

@app.get("/soma")
def soma():
    return {"2+2=4"}