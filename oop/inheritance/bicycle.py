class Bicycle:
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def applyBreak(self, decrement):
        self.speed -= decrement

    def speedUp(self, increment):
        self.speed += increment

