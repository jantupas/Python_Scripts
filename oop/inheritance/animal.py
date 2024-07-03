class Animal:
    alive = True

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def eat(self):
        print(f"This animal is called {self.name}, size {self.size}, and eating")

    def sleep(self):
        print(f"This animal is called {self.name}, size {self.size}, and sleeping")
