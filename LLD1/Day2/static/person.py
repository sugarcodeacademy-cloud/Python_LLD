class Person:
    #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "is eating ")

    @staticmethod
    def sleep():
        print("Person is sleeping")
