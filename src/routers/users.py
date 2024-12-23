from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()

@router.get("/")
async def get_users():
    from src.main import app
    cache_key = "users"
    cache_data = await app.redis.get(cache_key)
    if cache_data:
        return cache_data
    return {"message": "Anderson"}