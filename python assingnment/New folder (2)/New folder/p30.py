""" 
What relationship is appropriate for Student and Person?
the relationship between Student and Person is typically an inheritance relationship. This means that Student is a subclass of Person, inheriting its attributes and behaviors, while also adding or modifying specific attributes and behaviors unique to Student.
"""

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

class Student(Person):
    def __init__(self, name, age, address, student_id, courses):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.courses = courses

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}, Courses: {self.courses}"


person = Person("Dipak", 30, "ahmedabad")
student = Student("sagar", 20, "ahemedabad", "1", ["react js", "python"])

print(person)
print(student)
