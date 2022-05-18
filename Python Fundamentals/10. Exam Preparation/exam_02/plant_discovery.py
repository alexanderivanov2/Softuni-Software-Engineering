n = int(input())
plants = {}

for i in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    if plant not in plants:
        plants[plant] = {'rarity': rarity, 'rating': []}
    else:
        plants[plant]['rarity'] = rarity

command = input()

while not command == "Exhibition":
    action, *data = command.split(": ")

    if action == "Rate":
        plant, rating = data[0].split(' - ')

        if plant in plants:
            plants[plant]['rating'].append(rating)
        else:
            print('error')

    elif action == "Update":
        plant, rarity = data[0].split(' - ')
        if plant in plants:
            plants[plant]['rarity'] = int(rarity)
        else:
            print("error")
    elif action == "Reset":
        plant = data[0]
        if plant in plants:
            plants[plant]['rating'] = []
        else:
            print('error')
    command = input()

for key in plants:
    if plants[key]['rating']:
        plants[key]['rating'] = sum([float(rate) for rate in plants[key]['rating']]) / len(plants[key]['rating'])
    else:
        plants[key]['rating'] = 0

sorted_plants = dict(sorted(plants.items(), key=lambda x: (-x[1]["rarity"], -x[1]["rating"])))

print("Plants for the exhibition:")
for key, value in sorted_plants.items():
    print(f"- {key}; Rarity: {sorted_plants[key]['rarity']}; Rating: {sorted_plants[key]['rating']:.2f}")