'''
class Student:
    def __init__(self,ID,Name,Department):




     s1=Student('Steve','4A23','Information Engineering')
     s1.save_to_database
     s2=Student('Meg','2C33','Information management')    
     '''

class Student:
    def __init__(self,ID,Name,Department):
        self._ID=ID
        self._Name=Name
        self._Department=Department

class Teacher:
    pass

class Course:
    def __init__def(self, CourseCode, CourseName, Point, Type, Teacher, CourseTime):
        self._Course=Course
        


s1 = Student('4B22','Steve','Information Engineering')
print("Student s1's Name=",s1._Name)
print("Student s1's ID=",s1._ID)
print("Student s1's Department=",s1._Department)

s2=Student('4A14','Alex','Information management')
print("Student s2's Name=",s2._Name)
print("Student s2's ID=",s2._ID)
print("Student s2's Department=",s2._Department)

class  Student_Engineering(Student):
    def __init__(self,ID,Name,Department,math):
        super(). __init__(self,ID,Name,Department)