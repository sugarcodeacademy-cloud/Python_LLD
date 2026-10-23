from typing import Set

from LLD2.Builder.Student import Student
# from LLD2.Builder.StudentBuilder import StudentBuilder

# s1 = Student("Alex", 31, 24, 83.4, "Woxsen", 7866526567, "CSE", 2012)
#
# print(s1.age)

# Verbose
# studentBuilder1 = StudentBuilder()
# studentBuilder1.set_age(24)
# studentBuilder1.set_grad_year(2024)
# studentBuilder1.set_name("Priya")
# studentBuilder1.set_university_name("Woxsen University")
#
# student1 = Student(studentBuilder1)
# print(student1._name)

#VERBOSE
# builder = Student.getBuilder() #Student is responsible for creating a builder which validates and builds student object
# builder.set_name("Priya")
# builder.set_age(24)
# builder.set_university_name("Harvard")
# builder.set_grad_year(2024)
# student1 = builder.build() #Builder will validate and create a student object

student1 = (Student.getBuilder()
            .set_name("Bhavya")
            .set_age(24)
            .set_grad_year(2024)
            .set_university_name("Woxsen University")
            .build())

# builder1 = Student.getBuilder()
# builder2 = builder1.set_name("Alex")
# builder3 = builder2.set_university_name("MVSR")

print(student1._name)






