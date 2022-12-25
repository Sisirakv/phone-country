from typing import List
from fastapi import FastAPI
from models import Phone
from phone_iso3166.country import *


app = FastAPI()

db: List[Phone] = [
   
]

@app.get("/")
async def root():
    return {"Hello":"World"}

@app.get("/get-phone-country")
async def fetch_user():
    return db;

@app.post("/get-phone-country")
async def register_user(user:Phone):
    user.country = phone_country(user.phone)
    db.append(user.phone)
    db.append(user.country)
    return {"Phone":user.phone, "Country":user.country}
