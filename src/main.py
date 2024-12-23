from fastapi import FastAPI
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import redis.asyncio as aioredis

from src.config import settings
from src.routers import users, products  

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"Start application"}

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.MONGO_URI)
    app.db = app.mongodb_client["portfolio_db"]
    app.redis = await aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", decode_responses=True
    )

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
    await app.redis.close()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
