class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = {}

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons.values():
            return "This pokemon is already caught"
        self.pokemons[pokemon.name] = pokemon
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        if pokemon_name in self.pokemons:
            self.pokemons.pop(pokemon_name)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        first_line = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        second_line = ""
        for value in self.pokemons.values():
            second_line += f"- {value.pokemon_details()}\n"

        return first_line + second_line