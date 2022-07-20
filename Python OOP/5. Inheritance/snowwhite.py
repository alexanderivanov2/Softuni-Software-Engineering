dwarfs = {}
given_dwarf = input()
colors_hat = {}
while not given_dwarf == "Once upon a time":
    name, color, physics = given_dwarf.split(" <:> ")

    key = f"({color}) {name}"
    value = int(physics)
    if key not in dwarfs:
        if color not  in colors_hat:
            colors_hat[color] = 1
        else:
            colors_hat[color] += 1
        dwarfs[key] = [value, color]
    else:
        dwarfs[key][0] = max(dwarfs[key][0], value)

    given_dwarf = input()

sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda x: (-x[1][0], colors_hat[x[1][1]])))

for key, value in sorted_dwarfs.items():
    print(f"{key} <-> {value[0]}")