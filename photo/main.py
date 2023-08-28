from fastapi import FastAPI, UploadFile, File
from pymongo import MongoClient
import base64
from bson import ObjectId
from fastapi.responses import StreamingResponse
import io


app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["UserDB"]
collection = db["photos"]

@app.post("/upload/")
async def upload_photo(file: UploadFile = File(...)):
    photo_data = file.file.read()
    encoded_photo = base64.b64encode(photo_data).decode("utf-8")

    photo_doc = {
        "name": "自拍",
        "data": encoded_photo
    }

    collection.insert_one(photo_doc)

    return {"message": "成功"}

@app.get("/photos/{photo_id}")
async def get_photo(photo_id: str):
    photo = collection.find_one({"_id": ObjectId(photo_id)})

    if photo:
        name = photo["name"]
        data = base64.b64decode(photo["data"])
        return StreamingResponse(io.BytesIO(data), media_type="image/jpeg", headers={"Content-Disposition": f"attachment; filename={name}.jpg"})
    else:
        return {"error": "照片未找到。"}