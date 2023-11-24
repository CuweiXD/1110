
class Student:
    def __init__(self, name, gender, ID):
       self.name = name
       self.gender = gender
       self.ID = ID

    def __str__(self):
       return f"Name: {self.name}\nGender: {self.gender}\nID: {self.ID}"

A1 = Student("Herry", "Male", "4B1G0111")
print(A1)

A2 = Student("Mike", "Male", "4B1C0154")
print(A2)

A3 = Student("Merry", "Female", "4B1A0151")
print(A3)





'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nAge = {self.age}"

p1 = Person("John", 24)
print(p1)

p2 = Person("Ghost", 35)
print(p2.__dict__)

p3 = Person("Merry", 18)
print(p3)
'''


