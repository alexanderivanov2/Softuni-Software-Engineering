import unicodedata
from collections import deque


def check(fireworks):
    return all([value >= 3 for value in fireworks.values()])


firework_effect = deque(int(el) for el in input().split(", "))
explosive_power = [int(el) for el in input().split(", ")]
fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

while firework_effect and explosive_power:
    if firework_effect[0] <= 0:
        firework_effect.popleft()
        continue

    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    final_effect = firework_effect[0] + explosive_power[-1]

    if final_effect % 5 == 0 and final_effect % 3 == 0:
        fireworks['Crossette Fireworks'] += 1
        firework_effect.popleft()
        explosive_power.pop()
    elif final_effect % 3 == 0:
        fireworks['Palm Fireworks'] += 1
        firework_effect.popleft()
        explosive_power.pop()
    elif final_effect % 5 == 0:
        fireworks['Willow Fireworks'] += 1
        firework_effect.popleft()
        explosive_power.pop()
    else:
        firework_effect[0] -= 1
        firework_effect.append(firework_effect.popleft())

    if check(fireworks):
        print("Congrats! You made the perfect firework show!")
        break

if not check(fireworks):
    print(f"Sorry. You can’t make the perfect firework show.")
if firework_effect:
    print(f'Firework Effects left: {", ".join(map(str, firework_effect))}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(map(str, explosive_power))}')

for key, value in fireworks.items():
    print(f"{key}: {value}")
