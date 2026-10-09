# class Student:
#     universityName = "Harvard"
#     @staticmethod
#     def checkMarks(marks):
#         if marks < 35:
#             print("Student cannot be admitted")
#         else:
#             print("student is admitted")
#
#     @classmethod
#     def changeUniversity(cls, newUniversityName):
#         cls.universityName = newUniversityName
#
#
# Student.checkMarks(34)
#
# vinod = Student()
# bhavya = Student()
# Student.changeUniversity("Harvard University")
# print(vinod.universityName)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14*self.radius**2

    @property
    def diameter(self):
        return 2*self.radius

circle1 = Circle(4)
print(circle1.area)
print(circle1.diameter)




