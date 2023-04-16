from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from datetime import datetime
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List

router = APIRouter(prefix="/api")

client = MongoClient("mongodb+srv://jimmyjimmy0226:UcdSNPi9L7U$QM8@cluster0.gsg1p6n.mongodb.net/test")
db = client["fhsh_shop"]
items = db["items"]


class Item(BaseModel):
    name: str = ""
    summary : str = ""
    price: int = 0
    quantity: int = 0


@router.post("/create_item")
async def create_item(create: Item):

    if items.find_one({"name":create.name}):
        raise HTTPException(status_code=400, detail="The product already exists")
    if create.name == "":
        raise HTTPException(status_code=400, detail="No Item name entered")
    if create.summary == "":
        raise HTTPException(status_code=400, detail="No Item summary entered")
    if create.price == "":
        raise HTTPException(status_code=400, detail="No Item price entered")
    if create.quantity == "":
        raise HTTPException(status_code=400, detail="No Item price entered")    

    create_data = {
        "name": create.name,
        "summary": create.summary,
        "price": create.price,
        "quantity": create.quantity
    }

    result = items.insert_one(create_data)

    return {
        "id": str(result.inserted_id),
        "name": create_data["name"],
        "summary": create_data["summary"],
        "price": create_data["price"],
        "quantity": create_data["quantity"]
    }


@router.get("/read_item/{item_id}")
async def read_item(item_id: str):
    item = items.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "summary": item["summary"],
        "price": item["price"],
        "quantity": create_data["quantity"]
    }


@router.put("/update_item/{item_id}")
async def update_item(item_id: str, item: Item):
    existing_item = items.find_one({"_id": ObjectId(item_id)})
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")

    item_data = {
        "name": item.name,
        "summary": item.summary,
        "price": item.price,
        "quantity": item.quantity
    }

    items.update_one({"_id":ObjectId(item_id)}, {"$set": item_data})

    return {
        "id": item_id,
        "name": item_data["name"],
        "summary": item_data["summary"],
        "price": item_data["price"],
        "quantity": create_data["quantity"]
    }


@router.delete("/delete_item/{item_id}")
async def delete_item(item_id: str):
    delete = items.delete_one({"_id": ObjectId(item_id)})
    if not delete:
        raise HTTPException(status_code=404, detail="Item not found")
    items.delete_one({"_id": ObjectId(item_id)})
    return {
        "id": item_id,
        "message": "Item deleted"
    }

