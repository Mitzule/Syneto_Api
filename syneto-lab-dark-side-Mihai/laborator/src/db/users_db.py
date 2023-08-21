import json
import os
import sqlite3

from src.domain.users_domain import User

class UserDb:
    
    def __init__(self): #dunder method
        self.con, self.cur = self.open_Databse()
        self.table_user()
    
    def open_Databse(self):
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
                email TEXT,
                weight INTEGER,
                height INTEGER
            );
        """)
        self.con.commit()

    def add_user(self, user: User):
            
        username = user.username
        email = user.email
        weight = int(user.weight)
        height = int(user.height)
        
        self.cur.execute(f"""
            INSERT INTO user VALUES
                (   '{username}',
                    '{email}',
                    {weight},
                    {height}); 
            """)
        
        self.con.commit()


    def delete_user(self, user_name: str):

        uname = user_name
        self.cur.execute(f"""
            DELETE FROM user  WHERE username = '{uname}';
        """)
        self.con.commit()


    def edit_user(self, username: str, user: User): 
        
        uname = username
        email = user.email
        weight = user.weight
        height = user.height

        self.cur.execute(f""" 
                    UPDATE user 
                    SET email = '{email}', 
                        weight = '{weight}', 
                        height = '{height}' 
                    WHERE username = '{uname}';
                    """)
        self.con.commit()
        
        
    def select_users(self):
        
        self.cur.execute("SELECT * FROM user;")
        return self.cur.fetchall()
        