import sqlite3
import datetime
import requests
import json

from datetime import datetime, timedelta
from src.domain.users_domain import User
from src.domain.users_domain import Meal

class UserDb:
    def __init__(self):
        self.con, self.cur = self.open_Database()
        self.table_user()
        self.table_meal()
    
    def open_Database(self):
        try:
            con = sqlite3.connect("syneto.db")
            cur = con.cursor()
        except sqlite3.Error:
            print("Error opening database")
        return con, cur
    
    def table_user(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS user(
                username TEXT PRIMARY KEY,
                email TEXT UNIQUE,
                weight INTEGER,
                height INTEGER,
                birthday TEXT
            );
        """)
        self.con.commit()
        
    def table_meal(self):
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS meal(
                    username TEXT,
                    meal_name TEXT,
                    date TEXT,
                    calories INTEGER,
                    nutritional_value TEXT
                );
            """)
            self.con.commit()       

    def add_user(self, user: User):
        username = user.username
        email = user.email
        weight = int(user.weight)
        height = int(user.height)
        birthday = user.birthday
        
        if not self.is_username_unique(username):
            raise ValueError("Username already exists")
        
        if not self.is_email_unique(email):
            raise ValueError("Email already exists")
        
        self.cur.execute(
            """
            INSERT INTO user (username, email, weight, height, birthday)
            VALUES (?, ?, ?, ?, ?)
            """,
            (username, email, weight, height, birthday),
        )
        self.con.commit()
        
    def is_username_unique(self, username: str) -> bool:
        self.cur.execute("SELECT * FROM user WHERE username = ?", (username,))
        result = self.cur.fetchone()
        return result is None

    def is_email_unique(self, email: str) -> bool:
        self.cur.execute("SELECT * FROM user WHERE email = ?", (email,))
        result = self.cur.fetchone()
        return result is None        

    def delete_user(self, username: str):
        self.cur.execute(
            """
            DELETE FROM user WHERE username = ?
            """,
            (username,),
        )
        self.con.commit()

    def edit_user(self, username: str, user: User):
        email = user.email
        weight = int(user.weight)
        height = int(user.height)
        birthday = user.birthday

        self.cur.execute(
            """ 
            UPDATE user 
            SET email = ?, weight = ?, height = ?, birthday = ?
            WHERE username = ?
            """,
            (email, weight, height, birthday, username),
        )

        self.con.commit()

    def select_users(self):
        self.cur.execute("SELECT * FROM user;")
        return self.cur.fetchall()
    
    def select_users_name_email(self):
        self.cur.execute("SELECT username, email FROM user;")
        return self.cur.fetchall()
    
    def display_user_info(self, username: str):
        self.cur.execute("SELECT * FROM user WHERE username = ?", (username,))
        user_data = self.cur.fetchone()
        
        if user_data:
            username, email, weight, height, birthday = user_data
            
            birth_date = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()
            current_date = datetime.date.today()
            age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
            
            user_info = {
                "username": username,
                "email": email,
                "weight": weight,
                "height": height,
                "birthday": birthday,
                "age": age
            }
            return user_info

    def user_add_meal_to_profile(self, username: str, meal: Meal):
        uname = username
        meal_name = meal.name
        date = meal.date
        calories = 0
        nutritional_value = ""
        
        query = meal_name
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'zduTvlSzuNrRqhEztMZXoA==uULzTTKSkNIZEapU'})

        if response.status_code == requests.codes.ok:
            data = response.json()

            for item in data:
                cal = item["calories"]
                calories += cal
                
            nutritional_value = json.dumps(data, indent=4)
            self.cur.execute("INSERT INTO meal (username, meal_name, date, calories, nutritional_value) VALUES (?, ?, ?, ?, ?)", (uname, meal_name, date, calories, nutritional_value))
            
            self.con.commit()

        else:
            print("Error:", response.status_code, response.text)
            
    def user_display_meal(self, username: str):
        self.cur.execute("SELECT * FROM meal WHERE username = ?", (username,))
        return self.cur.fetchall()
    

    def user_querry_meal(self, username: str, start_date: datetime, end_date: datetime):
        uname = username
        start_date = start_date
        end_date = end_date
        
        self.cur.execute("SELECT * FROM meal WHERE username = ? AND date BETWEEN ? AND ?", (uname, start_date, end_date))
        
        return self.cur.fetchall()

    def user_delete_meal_from_profile(self, username: str, meal_name: str, date: str):
        uname = username
        meal_name = meal_name
        self.cur.execute("SELECT * FROM meal WHERE username=? AND date=?", (uname, date))
        meal = self.cur.fetchone()

        if meal is not None:
            self.cur.execute("DELETE FROM meal WHERE username=? AND meal_name=? AND date=?", (uname, meal_name, date))
            self.con.commit()
        else:
            print("Meal not found.")
            




    def user_edit_meal_from_profile(self, username: str, meal_name: str, date: str, new_meal_name: str, new_date: str):
        
        uname = username
        query = meal_name
        
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'zduTvlSzuNrRqhEztMZXoA==uULzTTKSkNIZEapU'})

        if response.status_code == requests.codes.ok:
            data = response.json()

            calories = 0
            for item in data:
                cal = item["calories"]
                calories += cal

            nutritional_value = json.dumps(data, indent=4)

            # Update the meal in the database with the new name and date
            self.cur.execute("UPDATE meal SET meal_name=?, date=?, calories=?, nutritional_value=? WHERE username=? AND meal_name=? AND date=?",
                            (new_meal_name, new_date, calories, nutritional_value, uname, meal_name, date))
            self.con.commit()
            print("Meal updated successfully.")
        else:
            print("Error:", response.status_code, response.text)
            
    def user_display_meal_calories_nutritional_value_date(self, username: str, date: str):
        self.cur.execute("SELECT meal_name, calories, nutritional_value FROM meal WHERE username=? AND date=?", (username, date))
        return self.cur.fetchall()

    def user_display_meal_calories_nutritional_value_period(self, username: str, start_date: str, end_date: str):
        self.cur.execute("SELECT meal_name, calories, nutritional_value FROM meal WHERE username=? AND date BETWEEN ? AND ?", (username, start_date, end_date))
        return self.cur.fetchall()