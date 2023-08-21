import json

from src.db.users_db import UserDb

class UserRepository:
    def __init__(self, persistance):
        self.persistance = persistance
        
    def select(self):
        return self.persistance.select_users()
    
    def select_name_email(self):
        return self.persistance.select_users_name_email()
        
    def display_user_info(self, username: str):
        return self.persistance.display_user_info(username)
    
    def add(self, user):
        return self.persistance.add_user(user)
        
    def delete(self, user_name):
        return self.persistance.delete_user(user_name)
        
    def edit(self, username, user):
        return self.persistance.edit_user(username, user)
    
    def add_meal(self, username, meal):
        return self.persistance.user_add_meal_to_profile(username, meal)
    
    def get_meals(self, username):
        return self.persistance.user_display_meal(username)
    
    def meal_query(self, username, start_date, end_date):
        return self.persistance.user_querry_meal(username, start_date, end_date)
    
    def delete_meal(self, username, meal_name, date):
        return self.persistance.user_delete_meal_from_profile(username, meal_name, date)
    
    def edit_meal(self, username, meal_name, date, new_meal_name, new_date):
        return self.persistance.user_edit_meal_from_profile(username, meal_name, date, new_meal_name, new_date)
    
    def display_meal_info(self, username, date):
        return self.persistance.user_display_meal_calories_nutritional_value_date(username, date)
    
    def display_meal_period(self, username, start_date, end_date):
        return self.persistance.user_display_meal_calories_nutritional_value_period(username, start_date, end_date)
    
    
#user repo receives in constructor an object whichknows how to save the users in a file or database
#create a config.json in which we telll what type of persistance we have


        


