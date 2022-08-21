from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successfully_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type, name):
        is_astro_exist = self.astronaut_repository.find_by_name(name)
        if is_astro_exist:
            return f"{name} is already added."
        astro_create_map = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}
        if astronaut_type not in astro_create_map:
            raise Exception("Astronaut type is not valid!")
        self.astronaut_repository.astronauts.append(astro_create_map[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        is_planet_exist = self.planet_repository.find_by_name(name)
        if is_planet_exist:
            return f"{name} is already added."
        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.planets.append(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        is_exist = self.astronaut_repository.find_by_name(name)
        if not is_exist:
            raise Exception(f"Astronaut {name} doesn't exists!")
        self.astronaut_repository.astronauts.remove(is_exist)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        is_planet_exist = self.planet_repository.find_by_name(planet_name)
        if not is_planet_exist:
            raise Exception("Invalid planet name!")
        sort_astros = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)
        if len(sort_astros) > 5:
            sort_astros = sort_astros[0:5]
        search_astros = [a for a in sort_astros if a.oxygen > 30]
        if len(search_astros) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        # sort_astros = sorted(sort_astros, key=lambda x: x.oxygen)
        # print(",".join(str(s.oxygen) for s in sort_astros))
        planet = is_planet_exist
        out_of_space = 0
        for astro in search_astros:
            out_of_space += 1
            while True:
                if not planet.items:
                    self.successfully_missions += 1
                    return f"Planet: {planet_name} was explored. {out_of_space} astronauts participated in collecting items."
                astro.backpack.append(planet.items.pop())
                astro.breathe()
                if astro.oxygen <= 0:
                    break
        self.not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        message = f"{self.successfully_missions} successful missions!\n{self.not_completed_missions} missions were not completed!\nAstronauts' info:\n"
        for astro in self.astronaut_repository.astronauts:
            message += f"Name: {astro.name}\nOxygen: {astro.oxygen}\nBackpack items: {'none' if not astro.backpack else ', '.join(astro.backpack)}\n"
        return message

# a = SpaceStation()
# a.add_astronaut("Geodesist", "A")
# a.add_astronaut("Meteorologist", "B")
# a.add_astronaut("Biologist", "C")
# a.add_astronaut("Biologist", "D")
# a.add_astronaut("Biologist", "E")
# a.add_astronaut("Biologist", "G")
# a.add_planet("ABC", "a, b, c, d, e, j, k")
# print(a.send_on_mission("ABC"))
# print(a.report())
