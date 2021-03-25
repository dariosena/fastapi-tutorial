from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=80
    )
    price: float = Field(..., gt=0,
                         description="The price must be greater than zero")
    tax: Optional[float]


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


app = FastAPI()


@app.post("/items")
async def create_item(item: Item):
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {
        "item_id": item_id,
        "item": item,
        "user": user
    }

    return results
