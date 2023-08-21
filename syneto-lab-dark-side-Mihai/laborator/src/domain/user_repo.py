import json
from src.db.users_db_json import UserJson
from src.db.users_db import UserDb

class UserRepository:
    def __init__(self, persistance):
        self.persistance = persistance
        
    def select(self):
        return self.persistance.select_users()
        
    def add(self, user):
        return self.persistance.add_user()
        
    def delete(self, user_index):
        return self.persistance.delete_user()
        
    def edit(self, username, user):
        return self.persistance.edit_user()
        
    
        
        
                
    
                
            
    
    
                
                
            
                
        

        
    
    
    

#user repo receives in constructor an object whichknows how to save the users in a file or database


#create a config.json in which we telll what type of persistance we have


        


