from pydantic import BaseModel

class User(BaseModel):
    username: str 
    email: str 
    height: int 
    weight: int 
    birthday: str 

class Meal(BaseModel):
    name: str 
    date: str
    calories: int
    nutritional_value: str