from abc import ABC, abstractmethod

class Programmer(ABC):
    
    @abstractmethod
    
    def calculate_salary(self):
        pass
    
class Senior_Programmer(Programmer):
    
    def calculate_salary(self):
        return 10000
    

    