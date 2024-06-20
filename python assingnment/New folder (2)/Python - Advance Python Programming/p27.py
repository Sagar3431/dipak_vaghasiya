""" 
What is Instantiation in terms of OOP terminology?
In object-oriented programming (OOP), instantiation refers to the process of creating a specific instance of a class.
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


my_car = Car("Toyota", "Corolla", 2020)

# Using the instance
print(my_car.display_info())  
