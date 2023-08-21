class Engine:
    def start(self):
        x= 2*2
        print(x)
        
class Wheels:
    def roll(self):
        print("Rolling")

class Car:
    def __init__(self, model : str, color : str):
        self.model = model
        self.color = color
        self.engine = Engine()
        self.wheels = Wheels()
        
    def start(self):
        self.engine.start()
        self.wheels.roll()
        
car = Car("Tesla", "rosu")
car.start()