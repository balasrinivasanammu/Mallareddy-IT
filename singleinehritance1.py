# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Child Class
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return super().__str__() + f", Grade: {self.grade}"

# Creating an object of Student
student = Student("Balaji", 20, "A")
print(student)

