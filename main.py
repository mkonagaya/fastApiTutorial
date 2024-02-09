import logging

from fastapi import FastAPI

from db.connectDb import connect_db

logging.basicConfig(level=logging.DEBUG,
                    filename='fastApi.log',
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

connect_db()
app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/item/{item_id}")
async def find_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
