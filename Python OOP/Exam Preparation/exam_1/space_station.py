from exam_1.astronaut.astronaut_repository import AstronautRepository
from exam_1.astronaut.biologist import Biologist
from exam_1.astronaut.geodesist import Geodesist
from exam_1.astronaut.meteorologist import Meteorologist
from exam_1.planet.planet import Planet
from exam_1.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.success = 0
        self.not_complete = 0
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type, name):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        elif astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")
        astro = None
        if astronaut_type == "Biologist":
            astro = Biologist(name)
        elif astronaut_type == "Geodesist":
            astro = Geodesist(name)
        else:
            astro = Meteorologist(name)
        self.astronaut_repository.add(astro)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astro = self.astronaut_repository.find_by_name(name)
        if not astro:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astro)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")
        astro_list = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)
        if len(astro_list) > 5:
            astro_list = astro_list[0:5]
        astro_list = [a for a in astro_list if a.oxygen > 30]
        if len(astro_list) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        planet = self.planet_repository.find_by_name(planet_name)
        # astro_list = [astro for astro in self.astronaut_repository.astronauts if astro.oxygen > 30]
        # if not astro_list:
        #     raise Exception("You need at least one astronaut to explore the planet!")
        # astro_list = sorted(astro_list)[::-1]
        # if len(astro_list) > 5:
        #     astro_list = astro_list[0:5]
        out_of_space = 0
        for astro in astro_list:
            out_of_space += 1
            while True:
                if not planet.items:
                    self.success += 1
                    return f"Planet: {planet_name} was explored. {out_of_space} astronauts participated in collecting items."
                astro.backpack.append(planet.items.pop())
                astro.breathe()
                if astro.oxygen <= 0:
                    break
        self.not_complete += 1
        return "Mission is not completed."

    def report(self):
        message = f"{self.success} successful missions!\n{self.not_complete} missions were not completed!\nAstronauts' info:\n"
        for astro in self.astronaut_repository.astronauts:
            message += f"Name: {astro.name}\nOxygen: {astro.oxygen}\nBackpack items: {'none' if not astro.backpack else ', '.join(astro.backpack)}\n"
        return message
