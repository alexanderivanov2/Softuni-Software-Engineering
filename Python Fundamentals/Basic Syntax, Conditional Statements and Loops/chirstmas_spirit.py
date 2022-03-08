ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLANDS = 3
TREE_LIGHTS = 15

quantity = int(input())
days = int(input())
budget = 0
total_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ORNAMENT_SET * quantity
        total_spirit += 5
    if day % 3 == 0:
        budget += (TREE_SKIRT * quantity) + (TREE_GARLANDS * quantity)
        total_spirit += 13
    if day % 5 == 0:
        budget += TREE_LIGHTS * quantity
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        budget += TREE_SKIRT + TREE_GARLANDS + TREE_LIGHTS

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
