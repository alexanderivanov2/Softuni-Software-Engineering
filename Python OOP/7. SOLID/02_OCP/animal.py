class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def get_species(self):
        return self.species
    


def animal_sound(animals: list):
    for animal in animals:
        print(animal.sound)


animals = [Animal('cat', "meow-meow"), Animal('dog', "woaf-woaf"), Animal("Chicken", "Quo Quo")]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
