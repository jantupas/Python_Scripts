from graphic_object import GraphicObject


class Circle(GraphicObject):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def draw(self):
        print("Drawing a circle!")

    def resize(self):
        print("Resizing a circle!")

    def show_params(self):
        print(f"X: {self.x} Y: {self.y} Z: {self.z}")
