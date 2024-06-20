""" 
Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python?
Inheritance is a fundamental concept in object-oriented programming that allows a class (called a subclass or derived class) to inherit attributes and methods from another class (called a superclass or base class).
The __init__ method in Python is a special method called a constructor. It is automatically invoked when a new instance of a class is created. The purpose of the __init__ method is to initialize the object's attributes and perform any setup necessary when the object is instantiated.

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


person = Person("Alice", 30)
print(person.display_info()) 
