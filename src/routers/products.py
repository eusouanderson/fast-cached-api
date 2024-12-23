
from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/")
async def get_products():
    from src.main import app

    cache_key = "products"
    cached_data = await app.redis.get(cache_key)
    if cached_data:
        return {"products": cached_data}

    
    products = await app.db["products"].find().to_list(100)
    await app.redis.set(cache_key, products, ex=60)  #60 segundos
    return {"products": products}
