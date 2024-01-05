class Course:   
    def __init__(self, CourseName, CourseClass, Teacher, Point, CourseType):         #初始化物件的屬性值
        self._CourseName = CourseName   #物件"課程名字"的屬性等於傳入"課程名字"的屬性值
        self._CourseClass = CourseClass  #物件"課程班級"屬性等於傳入課程班級"的屬性值
        self._Teacher = Teacher  #物件"課程老師"屬性等於傳入"課程老師"的屬性值
        self._Point = Point  #物件"課程學分"屬性等於傳入"課程學分"的屬性值
        self._CourseType = CourseType  #物件"課程類型(選修或必修)"屬性等於傳入"課程類型(選修或必修)"的屬性值

    #顯示課程資訊
    def DisplayInfo(self):      
        print(f"Course Name: {self._CourseName}")
        print(f"Course Class: {self._CourseClass}")
        print(f"Teacher: {self._Teacher}")
        print(f"Point: {self._Point}")
        print(f"Course Type: {self._CourseType}")    

    #修改課程班級
    def ChangeClass(self, NewClass):
        self._CourseClass = NewClass

    #增加課程學分
    def AddPoint(self, PointAdd):
        self._Point = self._Point + PointAdd    


ClassA = Course('PE-Tennis', 'IE2A', 'Steve', 2, 'Required')       
ClassB = Course('English', 'IC1L', 'David', 2, 'Required')         
ClassC = Course('C# Programming', 'IE3B', 'Rex', 3, 'Elective')    

#Class A 
print("\n==========Course Info==========")
ClassA.DisplayInfo()

ClassA.ChangeClass('CS22')
print("\n==========Change Info==========")
print(f"Change course class to {ClassA._CourseClass}")
print("\n==========New Info==========")
ClassA.DisplayInfo()

ClassA.AddPoint(1)
print("\n==========Change Info==========")
print(f"Change points to {ClassA._Point}")
print("\n==========New Info==========")
ClassA.DisplayInfo()

#Class B
ClassB.DisplayInfo()

ClassB.ChangeClass('EQ2M')
print("\n==========Change Info==========")
print(f"Change course class to {ClassB._CourseClass}")
print("\n==========New Info==========")
ClassB.DisplayInfo()

#Class C
ClassC.DisplayInfo()

ClassC.ChangeClass('IE1C')
print("\n==========Change Info==========")
print(f"Change course class to {ClassC._CourseClass}")
print("\n==========New Info==========")
ClassC.DisplayInfo()

