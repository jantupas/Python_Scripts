# from rectangle import Rectangle
# from circle import Circle
from cat import Cat
from dog import Dog


# rect = Rectangle(4, 5)
# rect.draw()
# rect.resize()
# rect.show_params()

# circle = Circle(7, 8, 10)
# circle.draw()
# circle.resize()
# circle.show_params()

cat1 = Cat("Jan", 23)
dog1 = Dog("Edgar", 24, "Brown")

c_name = cat1.get_name()
c_age = cat1.get_age()

d_name = dog1.get_name()
d_age = dog1.get_age()
d_color = dog1.get_color()

print(f"Cat name: {c_name} Cat age: {c_age}")
cat1.make_sound()
print(f"Dog name: {d_name} Dog age: {d_age} Dog color: {d_color}")
dog1.make_sound()
