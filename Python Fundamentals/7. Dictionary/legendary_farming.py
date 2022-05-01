def print_result(final_dict):
    for key, value in final_dict.items():
        print(f"{key}: {value}")



key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
legendary = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
txt = input().split()
winner = False


while not winner:
    for i in range(0, len(txt), 2):
        key = txt[i + 1].lower()
        quantity = int(txt[i])
        if key in key_materials:
            key_materials[key] += quantity
            if key_materials[key] >= 250:
                winner = True
                print(f"{legendary[key]} obtained!")
                key_materials[key] -= 250
                break
        elif key not in junk:
            junk[key] = quantity
        else:
            junk[key] += quantity
    if winner:
        break
    txt = input().split()

key_materials_sorted = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
junk_sorted = dict(sorted(junk.items(), key=lambda x: x[0]))

print_result(key_materials_sorted)
print_result(junk_sorted)