D_HEALTH = 250
D_DAMAGE = 45
D_ARMOR = 10

dragons = {}
dragons_type = {}
n = int(input())
for i in range(n):
    d_type, name, dmg, hp, armor = input().split()
    dmg = D_DAMAGE if dmg == 'null' else int(dmg)
    hp = D_HEALTH if hp == "null" else int(hp)
    armor = D_ARMOR if armor == "null" else int(armor)
    if d_type not in dragons:
        dragons[d_type] = {name:{"damage": dmg, "health": hp, "armor": armor}}
        dragons_type[d_type] = {"damage": dmg, "health": hp, "armor": armor}
    elif name not in dragons[d_type]:
        dragons[d_type][name] = {"damage": dmg, "health": hp, "armor": armor}
        dragons_type[d_type]['damage'] += dmg
        dragons_type[d_type]['health'] += hp
        dragons_type[d_type]['armor'] += armor
    else:
        dragons_type[d_type]['damage'] += dragons[d_type][name]["damage"] - dmg
        dragons_type[d_type]['health'] += dragons[d_type][name]["health"] - hp
        dragons_type[d_type]['armor'] += dragons[d_type][name]["armor"] - armor
        dragons[d_type][name] = {"damage": dmg, "health": hp, "armor": armor}


for key, value in dragons.items():
    d = len(dragons[key])
    print(f"{key}::({dragons_type[key]['damage'] / d:.2f}/{dragons_type[key]['health'] / d:.2f}/{dragons_type[key]['armor'] / d:.2f})")
    sorted_current_dragons = dict(sorted(value.items(), key=lambda x: x[0]))
    for name, data in sorted_current_dragons.items():
        print(f"-{name} -> damage: {data['damage']}, health: {data['health']}, armor: {data['armor']}")
