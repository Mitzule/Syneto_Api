import json
import os
import sqlite3

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

from src.domain.users_domain import User

class UserJson:
    
    def add_user(user: User):
        
        list_users=[]
        try:
            with open("src/users.json", "r") as file:
                list_users=json.load(file) 
        except FileNotFoundError:
            with open("src/users.json", "w") as file:
                pass
        list_users.append(user.dict()) 
        with open("src/users.json", "w")as file:
            json.dump(list_users, file) 
            
            
    def delete_user(user_index: int):
        
        with open("src/users.json", "r") as file:
            data = json.load(file)
        if user_index < 0 or user_index >= len(data):
            return {f"User with index {user_index} not found."}
        data.pop(user_index)
        with open("src/users.json", "w") as file:
            json.dump(data, file)    
        return {f"User with index {user_index} has been deleted."}

    def edit_user(username: str, user: User): 
        
        with open("src/users.json", "r") as file:
            list_users = json.load(file)
        for user in list_users:
            if user["username"] == username:
                user["email"] = user.email
                user["height"] = user.height
                user["weight"] = user.weight
        with open("src/users.json", "w") as file:
            json.dump(list_users, file)
        return {"message": "User updated successfully"}


    def select_users():
        
        with open("src/users.json", "r") as file:
            list_users = json.load(file)
        return list_users