class PlanetRepository:

    def __init__(self):
        self.planets = []

    def add(self, planet):
        self.planets.append(planet)

    def remove(self, planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        searched_astro = [x for x in self.planets if x.name == name]
        if searched_astro:
            return searched_astro[0]
