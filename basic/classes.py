# Class is a blueprint for creating objets
# Objects has propeties and methods
# Almost everything in Python is an object

# Create class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extend class - inheritance
class Customer(User):
    def __init__(self, name, email, age):
        super().__init__(name, email, age)
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    # override
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Initialize user object
brad = User('Brad Traversy', 'brad@gamil.com', 37)
print(type(brad))
print(brad.name)
print(brad.email)
print(brad.age)
print(brad.greeting())
brad.has_birthday()
print(brad.greeting())

janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)
janet.set_balance(500)
print(janet.greeting())
