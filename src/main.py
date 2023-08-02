from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.users import User
from settings.database import users
from schema.schemas import list_serial
from bson import ObjectId


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get("/users/{target}")
async def search_users(target):
    searched_users = list_serial(users.find({'name': {'$regex': f"^(?i){target}"}}).limit(15))
    return searched_users
