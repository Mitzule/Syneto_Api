import json
import os

from fastapi import FastAPI
from fastapi import APIRouter

from src.db.users_db import UserDb
from src.db.users_db_json import UserJson

from src.domain.users_domain import User
from src.domain.user_repo import UserRepository


with open("src/config.json", "r") as file:
    config = json.load(file)
    if config["persistance"] == "json":
        user_persistance = UserJson()
    elif config["persistance"] == "db":
        user_persistance = UserDb()
    else:
        print("Invalid persistance type")

user_repo = UserRepository(user_persistance)

app = FastAPI()
user_roouter = APIRouter(prefix="/user")

@user_roouter.get("/GetUsers")
async def getUsers():
    return user_repo.select()


@user_roouter.post("/AddUser")
async def addUser_Post(user: User):
    return user_repo.add(user)


@user_roouter.delete("/{user_name}")
async def delete_user_delete(user_name: str):
    return user_repo.delete(user_name)


@user_roouter.put("/EditUser/{username}")
async def editUser_put(username: str, new_fields: User): 
    return user_repo.edit(username, new_fields)


