from animal import Animal
from rabbit import Rabbit
from bicycle import Bicycle
from mountainbike import Mountainbike

animal1 = Animal("Jed", "Small")
animal1.eat()
animal1.sleep()
rabbit1 = Rabbit("Jan", "Mini", 22)
rabbit1.eat()
rabbit1.sleep()
rabbit1.run()

bicycle1 = Bicycle(1, 100)

print(f"Gear: {bicycle1.gear} Speed: {bicycle1.speed}")
bicycle1.speedUp(5)
print(f"Gear: {bicycle1.gear} Speed: {bicycle1.speed}")
bicycle1.applyBreak(10)
print(f"Gear: {bicycle1.gear} Speed: {bicycle1.speed}")

mountainbike1 = Mountainbike(1, 100, "medium")
print(f"Gear: {mountainbike1.gear} Speed: {mountainbike1.speed} Seat Height: {mountainbike1.seat_height}")
mountainbike1.applyBreak(20)
print(f"Gear: {mountainbike1.gear} Speed: {mountainbike1.speed} Seat Height: {mountainbike1.seat_height}")
mountainbike1.speedUp(50)
print(f"Gear: {mountainbike1.gear} Speed: {mountainbike1.speed} Seat Height: {mountainbike1.seat_height}")
