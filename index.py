# Assignment 1
# Bass class
class Superhero:
    def __init__(self, name, real_name, power, city):
        self.name = name
        self.real_name = real_name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, also known as {self.real_name}. My superpower is {self.power}."

    def save_the_day(self):
        return f"{self.name} is saving the day in {self.city}!"

    def __str__(self):
        return f"{self.name} (Real Name: {self.real_name}, Power: {self.power}, City: {self.city})"
    
# subclass
class FlyingSuperhero(Superhero):
    def __init__(self, name, real_name, power, city, flight_speed):
        super().__init__(name, real_name, power, city)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} is flying at a speed of {self.flight_speed} mph!"

    def save_the_day(self):
        return f"{self.name} swoops in from the sky to save the day in {self.city}!"

class StrengthSuperhero(Superhero):
    def __init__(self, name, real_name, power, city, strength_level):
        super().__init__(name, real_name, power, city)
        self.strength_level = strength_level

    def lift(self, weight):
        if weight <= self.strength_level:
            return f"{self.name} lifts {weight} pounds effortlessly!"
        else:
            return f"{self.name} struggles to lift {weight} pounds!"

    def save_the_day(self):
        return f"{self.name} uses their incredible strength to save the day in {self.city}!"
    
# objects
# Create instances of superheroes
superman = FlyingSuperhero("Superman", "Clark Kent", "Super Strength and Flight", "Metropolis", 500)
hulk = StrengthSuperhero("Hulk", "Bruce Banner", "Incredible Strength", "New York", 1000)

# Introduce the superheroes
print(superman.introduce())
print(hulk.introduce())

# Demonstrate their unique abilities
print(superman.fly())
print(hulk.lift(800))
print(hulk.lift(1200))

# Show how they save the day
print(superman.save_the_day())
print(hulk.save_the_day())