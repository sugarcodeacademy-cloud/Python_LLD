# class StudentBuilder:
#     def __init__(self):
#         self._name = None
#         self._age = 0
#         self._grad_year = 0
#         self._university_name = None
#
#     def set_name(self, name):
#         self._name = name
#         return self
#
#
#     def set_age(self, age):
#         self._age = age
#         return self
#
#
#     def set_grad_year(self, grad_year):
#         self._grad_year = grad_year
#         return self
#
#     def set_university_name(self, university_name):
#         self._university_name = university_name
#         return self
#
#     def get_name(self):
#         return self._name
#
#     def get_age(self):
#         return self._age
#
#     def get_grad_year(self):
#         return self._grad_year
#
#     def get_university_name(self):
#         return self._university_name
#
#     def validate(self):
#         if self._age < 18 or self._age > 80:
#             raise ValueError("Invalid age")
#
#         if self._grad_year < 2016:
#             raise ValueError("Invalid graduation year")
#
#     def build(self):
#         self.validate()
#
#         from Student import Student
#         return Student(self)