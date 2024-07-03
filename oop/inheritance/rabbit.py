from animal import Animal


class Rabbit(Animal):

    def __init__(self, name, size, age):
        super().__init__(name, size)
        self.age = age

    def run(self):
        print(f"This animal is called {self.name}, size {self.size}, age, {self.age} and running")
