from collections import deque

presents = {"Bicycle": 0, "Doll": 0, "Teddy bear": 0, "Wooden train": 0}
materials = deque(int(el) for el in input().split())
magic_values = deque(int(el) for el in input().split())

while materials and magic_values:
    material, magic = materials.pop(), magic_values.popleft()
    if magic == 0 and material == 0:
        continue
    if material == 0:
        magic_values.appendleft(magic)
        continue
    if magic == 0:
        materials.append(material)
        continue
    total_magic = material * magic
    if total_magic < 0:
        materials.append(material + magic)
    elif total_magic == 150:
        presents["Doll"] += 1
    elif total_magic == 250:
        presents["Wooden train"] += 1
    elif total_magic == 300:
        presents["Teddy bear"] += 1
    elif total_magic == 400:
        presents["Bicycle"] += 1
    else:
        materials.append(material + 15)

if (presents["Doll"] != 0 and presents["Wooden train"] != 0) or (
        presents["Teddy bear"] != 0 and presents["Bicycle"] != 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(el) for el in reversed(materials))}")
if magic_values:
    print(f"Magic left: {', '.join(str(el) for el in magic_values)}")

for key, value in presents.items():
    if value > 0:
        print(f"{key}: {value}")