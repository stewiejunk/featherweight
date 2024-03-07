from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {"message": "Vetro API is up and running!"}