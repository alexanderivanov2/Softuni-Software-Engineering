from collections import deque

materials = [int(el) for el in input().split()]
magic_levels = deque([int(el) for el in input().split()])
gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while magic_levels and materials:
    material = materials.pop()
    magic = magic_levels.popleft()
    sums = magic + material
    if sums < 100:
        if sums % 2 == 0:
            sums = material * 2 + magic * 3
        else:
            sums *= 2
    elif sums > 499:
        sums /= 2

    if 99 < sums < 200:
       gifts["Gemstone"] += 1
    elif 199 < sums < 300:
        gifts["Porcelain Sculpture"] += 1
    elif 299 < sums < 400:
        gifts["Gold"] += 1
    elif 399 < sums < 500:
        gifts["Diamond Jewellery"] += 1


if (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0) or (gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(el) for el in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(el) for el in magic_levels)}")

gifts = dict(sorted(gifts.items(), key=lambda x: x[0]))

for key, value in gifts.items():
    if value > 0:
        print(f"{key}: {value}")