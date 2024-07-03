from graphic_object import GraphicObject


class Rectangle(GraphicObject):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self):
        print("Drawing a rectangle!")

    def resize(self):
        print("Resizing a rectangle!")
