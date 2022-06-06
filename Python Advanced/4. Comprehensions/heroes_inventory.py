def create_dictionary():
    heroes_dict = {}
    heroes2 = input().split(", ")
    for hero in heroes2:
        heroes_dict[hero] = {"Items": [], "Cost": 0}
    return heroes_dict


heroes = create_dictionary()

command = input()

while command != "End":
    hero, item, cost = command.split("-")
    if item not in heroes[hero]["Items"]:
        heroes[hero]["Items"].append(item)
        heroes[hero]["Cost"] += int(cost)
    command = input()

for k, v in heroes.items():
    print(f"{k} -> Items: {len(v['Items'])}, Cost: {v['Cost']}")
