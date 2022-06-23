from collections import deque


def check_ezio(bombs):
    return all(value >= 3 for value in bombs.values())


bomb_effect = deque(int(el) for el in input().split(", "))
bomb_casing = [int(el) for el in input().split(", ")]

bombs = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while bomb_effect and bomb_casing:
    combination = bomb_effect[0] + bomb_casing[-1]
    if combination == 40:
        bombs["Datura Bombs"] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    elif combination == 60:
        bombs["Cherry Bombs"] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    elif combination == 120:
        bombs["Smoke Decoy Bombs"] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5
        continue
    if check_ezio(bombs):
        print("Bene! You have successfully filled the bomb pouch!")
        break

if not check_ezio(bombs):
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effect)}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casing)}")
else:
    print("Bomb Casings: empty")

for bomb, count in bombs.items():
    print(f"{bomb}: {count}")
