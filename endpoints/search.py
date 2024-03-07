from fastapi import APIRouter, Query
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId 
import time

router = APIRouter()

with open("./uri.database", "r") as file:
    database = file.read()

@router.get("/search")
async def search(key: str = Query(..., description="Key to search for in the database"),
                 value: str = Query(..., description="Value associated with the key")):
    try:
        client = MongoClient(database)
        db = client.get_database("users")
        collection = db.get_collection("users")
        
        result = collection.find_one({key: value})
        
        if result:
            result["_id"] = str(result["_id"])

            return {"message": "Found Data", "result": result}
        else:
            return {"message": "Not Found"}
    except Exception as e:
        return {"message": "Error occurred", "error": str(e)}
