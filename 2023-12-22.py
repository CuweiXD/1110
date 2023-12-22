# -*- coding: utf-8 -*-

class Course:
    def __init__(self, CourseCode, CourseName, Point, CourseType, Teacher, CourseTime):
        self._CourseCode = CourseCode
        self._CourseName = CourseName
        self._Point = Point
        self._CourseType = CourseType
        self._Teacher = Teacher
        self._CourseTime = CourseTime


C1 = Course('EN154', 'Basic English', 2, 'Required', 'Steve', '8:00-9:50 AM')
print("[Course Introduction]")
print("Course Name:" ,C1._CourseName)
print("Course Code:" ,C1._CourseCode)
print("Point:" ,C1._Point)
print("Type:" ,C1._CourseType)
print("Course Teacher:" ,C1._Teacher)
print("Course Time:" ,C1._CourseTime)
