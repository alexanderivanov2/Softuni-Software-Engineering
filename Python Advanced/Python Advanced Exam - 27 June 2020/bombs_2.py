from collections import deque

effects = deque([int(el) for el in input().split(", ")])
casings = [int(el) for el in input().split(", ")]
bombs = {"Cherry": 0, "Datura": 0, "Smoke Decoy": 0}
make = True
complete = False


while effects and casings:
    value = effects[0] + casings[-1]
    if value == 40:
        bombs["Datura"] += 1
    elif value == 60:
        bombs["Cherry"] += 1
    elif value == 120:
        bombs["Smoke Decoy"] += 1
    else:
        make = False
        casings[-1] -= 5

    if make:
        effects.popleft()
        casings.pop()
    else:
        make = True


    if bombs["Cherry"] >= 3 and bombs["Datura"] >= 3 and bombs["Smoke Decoy"] >= 3:
        complete = True
        break

if complete:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join(str(el) for el in effects)}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join(str(el)for el in casings)}")
else:
    print("Bomb Casings: empty")


for key, value in bombs.items():
    print(f"{key} Bombs: {value}")