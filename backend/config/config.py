import os

from beanie import init_beanie
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

import models

load_dotenv()

mongodb_host = os.getenv('MONGODB_HOST')
mongodb_port = os.getenv('MONGODB_PORT')
mongodb_user = os.getenv('MONGODB_USER')
mongodb_password = os.getenv('MONGODB_PASSWORD')
mongodb_database = os.getenv('MONGODB_DATABASE')


async def initiate_database():
    client = AsyncIOMotorClient(f"mongodb://{mongodb_user}:{mongodb_password}@{mongodb_host}:{mongodb_port}")
    await init_beanie(
        database=client[mongodb_database]
        , document_models=models.__all__
    )
