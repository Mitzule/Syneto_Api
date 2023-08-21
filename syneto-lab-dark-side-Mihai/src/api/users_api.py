import json
import os

from fastapi import FastAPI
from fastapi import APIRouter

from src.db.users_db import UserDb
from src.domain.users_domain import User
from src.domain.users_domain import Meal
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
async def get_user():
    return user_repo.select()

@user_roouter.get("/GetUsersByNameEmail")
async def get_users_by_name_email():
    return user_repo.select_name_email()

@user_roouter.get("/DisplayUserInfo/{username}")
async def display_user_info():
    return user_repo.display_user_info()

@user_roouter.post("/AddUser")
async def add_user(user: User):
    return user_repo.add(user)

@user_roouter.delete("/DeleteUser/{username}")
async def delete_user(username: str):
    return user_repo.delete(username)

@user_roouter.put("/EditUser/{username}")
async def edit_user(username: str, new_fields: User): 
    return user_repo.edit(username, new_fields)

@user_roouter.post("/AddMeal/{username}")
async def user_add_meal_to_profile(username: str, meal: Meal):
    return user_repo.add_meal(username, meal)

@user_roouter.get("/GetMeals/{username}")
async def get_meals(username: str):
    return user_repo.get_meals(username)

@user_roouter.get("/QueryMeals/{username}")
async def query_meals(username: str, start_date: str, end_date: str):
    return user_repo.meal_query(username, start_date, end_date)

@user_roouter.delete("/DeleteMeal/{username}")
async def delete_meal(username: str, meal_name: str, date: str):
    return user_repo.delete_meal(username, meal_name, date)

@user_roouter.put("/EditMeal/{username}")
async def edit_meal(username: str, meal_name: str, date: str, new_meal_name: str, new_date: str):
    return user_repo.edit_meal(username, meal_name, date, new_meal_name, new_date)

@user_roouter.get("/DisplayMealInfo/{username}")
async def display_meal_info(username: str, date: str):
    return user_repo.display_meal_info(username, date)

@user_roouter.get("/DisplayMealPeriod/{username}")
async def display_meal_period(username: str, start_date: str, end_date: str):
    return user_repo.display_meal_period(username, start_date, end_date)