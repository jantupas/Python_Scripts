from abc import ABC, abstractmethod


class GraphicObject(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self):
        pass

    def show_params(self):
        print(f"X: {self.x} Y: {self.y}")
