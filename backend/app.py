import random
import string

from fastapi import FastAPI, Body

from config.config import initiate_database
from models.url import URLModel
from schemas.url import URLSchema, Response

app = FastAPI()


def generate_short_url(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


@app.put("/url", tags=["Shortening"], response_model=Response)
async def shorten_url(req: URLSchema = Body(...)):
    short_url = generate_short_url()
    url_document = URLModel(long=req.long, short=short_url)
    await url_document.insert()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Short URL generated",
        "data": req.long,
    }
