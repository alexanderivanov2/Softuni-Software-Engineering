from exam_3.aquarium.freshwater_aquarium import FreshwaterAquarium
from exam_3.aquarium.saltwater_aquarium import SaltwaterAquarium
from exam_3.decoration.decoration_repository import DecorationRepository
from exam_3.decoration.ornament import Ornament
from exam_3.decoration.plant import Plant
from exam_3.fish.freshwater_fish import FreshwaterFish
from exam_3.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        return "Invalid aquarium type."

        # may cause error

    def add_decoration(self, decoration_type):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        decor = self.decorations_repository.find_by_type(decoration_type)
        if aquarium and decor != "None":
            self.decorations_repository.remove(decor)
            aquarium[0].add_decoration(decor)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        elif decor == "None":
            return f"There isn't a decoration of type {decoration_type}."
        # can cause a error

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if aquarium:
            aquarium = aquarium[0]
            if aquarium.capacity == aquarium.current_fish:
                return "Not enough capacity."
            elif aquarium.A_TYPE[0] != fish_type[0]:
                return "Water not suitable."
            fish = None
            if fish_type == "FreshwaterFish":
                fish = FreshwaterFish(fish_name, fish_species, price)
            else:
                fish = SaltwaterFish(fish_name, fish_species, price)
            aquarium.add_fish(fish)
            return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if aquarium:
            aquarium = aquarium[0]
            count = len(aquarium.fish)
            aquarium.feed()
            return f"Fish fed: {count}"

    def calculate_value(self, aquarium_name):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        if aquarium:
            aquarium = aquarium[0]
            value = 0
            value += sum([f.price for f in aquarium.fish])
            value += sum([d.price for d in aquarium.decorations])
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        return "\n".join(str(a) for a in self.aquariums)


