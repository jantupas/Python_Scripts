class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setAddress(self, address):
        self.address = address

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getAddress(self):
        return self.address

    def greeting(self):
        return f"Hello! My name is {self.name}, my age is {self.age}, and I live in {self.address}"
