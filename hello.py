class Car:
    def __init__(self, model, name):
        self.model = model
        self.name = name 
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name


Car = Car("Ferarri", "Lambogene")

print(Car.get_name())