from fastapi import FastAPI
from typing import Union
app = FastAPI()
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id : int):
    return {"item_id": item_id}



@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    result = {"item_id": item_id, **item.dict()}
    return result

