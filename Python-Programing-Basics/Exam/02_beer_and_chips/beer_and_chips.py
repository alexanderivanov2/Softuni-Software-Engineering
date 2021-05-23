from math import ceil

fan_name = input()
budget = float(input())
bottles_beer = int(input())
packages_chips = int(input())

beers_cost = bottles_beer * 1.20
chips_cost = ceil((beers_cost * 0.45) * packages_chips)
total_cost = beers_cost + chips_cost

if budget >= total_cost:
    print(f"{fan_name} bought a snack and has {budget - total_cost:.2f} leva left.")
else:
    print(f"{fan_name} needs {total_cost - budget:.2f} more leva!")