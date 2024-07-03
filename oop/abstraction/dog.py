from animal import Animal


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def get_color(self):
        return self.color

    def make_sound(self):
        print("arf")
