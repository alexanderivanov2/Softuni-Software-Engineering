cities = {}

city = input()

while not city == "Sail":
    name, people, gold = city.split("||")
    people = int(people)
    gold = int(gold)
    if name not in cities:
        cities[name] = {'population': people, 'gold': gold}
    elif name in cities:
        cities[name]['population'] += people
        cities[name]['gold'] += gold
    city = input()

command = input()

while not command == "End":
    action, town, *data = command.split("=>")
    if action == "Plunder":
        gold = int(data[1])
        people = int(data[0])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= people
        cities[town]['gold'] -= gold
        if cities[town]["population"] == 0 or cities[town]['gold'] == 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    else:
        gold = int(data[0])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has { cities[town]['gold']} gold.")

    command = input()

if cities:
    sorted_cities_by_gold = dict(sorted(cities.items(), key=lambda x: (-x[1]['gold'], x)))
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, value in sorted_cities_by_gold.items():
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
