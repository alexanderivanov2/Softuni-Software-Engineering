houses = [int(el) for el in input().split("@")]

command = input()
index = 0
while not command == "Love!":
    jump = command.split()[1]
    jump = int(jump)
    if index + jump >= len(houses) or jump >= len(houses):
        index = 0
    else:
        index += jump

    if houses[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    elif houses[index] - 2 <= 0:
        houses[index] = 0
        print(f"Place {index} has Valentine's day.")
    else:
        houses[index] -= 2
    command = input()

print(f"Cupid's last position was {index}.")
if houses.count(0) == len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - houses.count(0)} places.")