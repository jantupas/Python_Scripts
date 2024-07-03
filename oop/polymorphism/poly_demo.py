from animal_sounds import AnimalSounds
from cow import Cow
from dog import Dog
from bird import Bird
from robin import Robin

animal_sound = AnimalSounds()
animal_sound.sound()

cow1 = Cow()
cow1.sound()

dog1 = Dog()
dog1.sound()
dog1.another_sound("angry")

bird1 = Bird()
bird1.sing()

robin1 = Robin()
robin1.sing()
robin1.sing_again()
