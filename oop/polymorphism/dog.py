from animal_sounds import AnimalSounds


class Dog(AnimalSounds):
    def sound(self):
        print("The dog says: bark bark")

    def another_sound(self, angry):
        super().sound()
