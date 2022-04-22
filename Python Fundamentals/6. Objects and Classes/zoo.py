class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, spice, name):
        if spice[0] == "m":
            self.mammals.append(name)
        elif spice[0] == "f":
            self.fishes.append(name)
        elif spice[0] == "b":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species[0] == "m":
            return print(f"Mammals in {self.name}: {', '.join(self.mammals)}")
        elif species[0] == "f":
            return print(f"Fishes in {self.name}: {', '.join(self.fishes)}")
        return print(f"Birds in {self.name}: {', '.join(self.birds)}")

    def total(self):
        return print(f"Total animals: {Zoo.__animals}")


zoo = Zoo(input())
n = int(input())

for i in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

kind = input()
zoo.get_info(kind)
zoo.total()