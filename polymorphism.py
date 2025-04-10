# Assignment 2
# base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# subclass
class Car(Vehicle):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def move(self):
        return f"{self.name} is driving 🚗"
    
class Bike(Vehicle):
    def __init__(self, name, type_of_bike):
        super().__init__(name)
        self.type_of_bike = type_of_bike

    def move(self):
        return f"{self.name} is pedaling 🚴"
    
class Plane(Vehicle):
    def __init__(self, name, airline):
        super().__init__(name)
        self.airline = airline

    def move(self):
        return f"{self.name} is flying ✈️"
    
# objects
# Create instances of vehicles
car = Car("Toyota", "Camry")
bike = Bike("Mountain Bike", "Off-road")
plane = Plane("Boeing 747", "Airways")

# Demonstrate their movement
print(car.move())
print(bike.move())
print(plane.move())