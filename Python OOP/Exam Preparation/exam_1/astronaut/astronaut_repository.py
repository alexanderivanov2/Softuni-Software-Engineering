class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        searched_astro = [x for x in self.astronauts if x.name == name]
        if searched_astro:
            return searched_astro[0]
