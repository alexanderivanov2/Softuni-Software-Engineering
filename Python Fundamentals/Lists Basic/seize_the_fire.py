HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

fires = input().split("#")
water = int(input())
effort = 0
cells = []

for fire in fires:
    type_fire, size =fire.split(" = ")
    size = int(size)
    if type_fire == "High" and size in HIGH and water >= size:
        cells.append(size)
        effort += size * 0.25
        water -= size
    elif type_fire == "Medium" and size in MEDIUM and water >= size:
        cells.append(size)
        effort += size * 0.25
        water -= size
    elif type_fire == "Low" and size in LOW and water >= size:
        cells.append(size)
        effort += size * 0.25
        water -= size
if cells:
    print("Cells:\n- ", end="")
    print('\n- '.join(str(cell) for cell in cells), end="\n")
else:
    print("Cells:")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells)}")