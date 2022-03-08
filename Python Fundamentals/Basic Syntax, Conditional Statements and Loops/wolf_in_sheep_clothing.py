list_animals = input().split(", ")
wolf_index = list_animals.index("wolf")


if wolf_index == len(list_animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len(list_animals) - 1 - wolf_index}! You are about to be eaten by a wolf!")

