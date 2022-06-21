from collections import deque

effect = deque([int(el) for el in input().split(",")])
power = [int(el) for el in input().split(",")]
fireworks = {"Palm": 0, "Willow": 0, "Crossette": 0}
make = True
show = False


while effect and power:
    if effect[0] <= 0 or power[-1] <= 0:
        if effect[0] <= 0 and power[-1] <= 0:
            effect.popleft()
            power.pop()
        elif effect[0] <= 0:
            effect.popleft()
        elif power[-1] <= 0:
            power.pop()
        continue

    value = effect[0] + power[-1]
    if value % 3 == 0 and not value % 5 == 0:
        fireworks["Palm"] += 1
    elif value % 5 == 0 and not value % 3 == 0:
        fireworks["Willow"] += 1
    elif value % 5 == 0 and value % 3 == 0:
        fireworks["Crossette"] += 1
    else:
        make = False

    if make:
        effect.popleft()
        power.pop()
    else:
        make = True
        curr_effect = effect.popleft() - 1
        if curr_effect > 0:
            effect.append(curr_effect)

    if fireworks["Palm"] >= 3 and fireworks["Willow"] >= 3 and fireworks["Crossette"] >= 3:
        show = True
        break


if show:
    print(f"Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effect:
    print(f"Firework Effects left: {', '.join(str(el) for el in effect)}")
if power:
    print(f"Explosive Power left: {', '.join(str(el) for el in power)}")

for key, value in fireworks.items():
    print(f"{key} Fireworks: {value}")