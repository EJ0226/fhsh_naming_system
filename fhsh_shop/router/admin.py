import uuid
from fastapi import APIRouter, HTTPException, Header
from pymongo import MongoClient
from pydantic import BaseModel, EmailStr, constr
from bson.objectid import ObjectId
from typing import List

router = APIRouter(prefix="/api")

client = MongoClient("mongodb+srv://jimmyjimmy0226:UcdSNPi9L7U$QM8@cluster0.gsg1p6n.mongodb.net/test")
db = client["fhsh_shop"]
users = db["users"]
items = db["items"]
orders = db["orders"]

class User_id(BaseModel):
    user_id : str

class User(BaseModel):
    username:str
    password:str
    is_admin: bool

@router.get("/admin/get_all_users")
async def get_all_users(user : User):
    if not user.is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized")
    users_list = []
    for user in users.find():
        user["_id"] = str(user["_id"])
        users_list.append(user)
    return users_list

@router.get("/admin/get_all_item")
async def get_all_item(user : User):
    if not user.is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized")
    item_list = []
    for item in items.find():
        item["_id"] = str(item["_id"])
        item_list.append(item)
    return item_list

@router.get("/admin/get_all_orders")
async def get_all_orders(user : User):
    if not user.is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized") 
    orders_list = []
    for order in orders.find():
        order["_id"] = str(order["_id"])
        orders_list.append(order)
    return orders_list

@router.get("/admin/get_user")
async def get_user(user_id: str, user: User):
    if not user.is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized")
    find_user = users.find_one({"_id": ObjectId(user_id)})
    if not find_user:
        raise HTTPException(status_code=404, detail="User not found")
    find_user["_id"] = str(find_user["_id"])
    return find_user

@router.get("/admin/get_item")
async def get_item(item_id: str, user: User):
    if not user.is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized") 
    find_item = items.find_one({"_id": ObjectId(item_id)})
    if not find_item:
        raise HTTPException(status_code=404, detail="Item not found")
    find_item["_id"] = str(find_item["_id"])
    return find_item

@router.get("/admin/get_order")
async def get_order(order_id: str, user: User):
    if not user.is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized")
    find_order = orders.find_one({"_id": ObjectId(order_id)})
    if not find_order:
        raise HTTPException(status_code=404, detail="Order not found")
    find_order["_id"] = str(find_order["_id"])
    return find_order

@router.delete("/admin/delete_user")
async def delete_user(user_id : str, user : User):
    if not user.is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized") 
    find_user = users.find_one({"_id": ObjectId(user_id)})
    if not find_user:
        raise HTTPException(status_code=404, detail="User not found") 
    users.delete_one({"_id": ObjectId(user_id)})
    return {"message": f"User {user_id} deleted successfully"}

@router.delete("/admin/delete_item")
async def delete_item(user : User):
    if not user.is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized")
    item = item.find_one({"_id": ObjectId(user.item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.delete_one({"_id": ObjectId(user.item_id)})
    return {"message": f"item {user.item_id} deleted successfully"}