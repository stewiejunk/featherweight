from fastapi import APIRouter
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import time

router = APIRouter()

with open("./uri.database", "r") as file:
    database = file.read()
    
@router.get("/ping")
async def ping():
    client = MongoClient(database, server_api=ServerApi("1"))

    try:
        start_time = time.time()
        client.admin.command("ping")
        end_time = time.time()
        latency = end_time - start_time

        return {"message": "Vetro Database successfully pinged!", "latency": f"{latency:.6f}s"}
    except Exception as e:
        print(e)
        return {"message": "Couldnt pinging the Database"}