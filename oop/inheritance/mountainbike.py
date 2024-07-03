from bicycle import Bicycle


class Mountainbike(Bicycle):
    def __init__(self, gear, speed, seat_height):
        super().__init__(gear, speed)
        self.seat_height = seat_height

    def inform(self):
        print(f"I am at {self.gear} gear and my current speed is {self.speed}")
