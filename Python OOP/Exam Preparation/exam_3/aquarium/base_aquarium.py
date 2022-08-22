from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    A_TYPE = "Base"

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []
        self.current_fish = 0
        # help may cause error

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        comfort = 0
        comfort += sum([d.comfort for d in self.decorations])
        return comfort

    def add_fish(self, fish):
        if self.current_fish == self.capacity:
            return "Not enough capacity."
        if fish.FISH_TYPE[0] == self.A_TYPE[0]:
            self.fish.append(fish)
            self.current_fish += 1
            return f"Successfully added {fish.FISH_TYPE} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)
            self.current_fish -= 1

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish = " ".join(f.name for f in self.fish) if self.fish else "none"
        message = f"{self.name}:\nFish: {fish}\nDecorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
        return message
