from collections import deque

people = deque()
quantity = int(input())

get_person = input()

while not get_person == "Start":
    people.append(get_person)
    get_person = input()

usage = input()

while not usage == "End":
    if "refill" in usage:
        liters = usage.split()[1]
        liters = int(liters)
        quantity += liters
    else:
        liters = int(usage)
        if liters <= quantity:
            print(f"{people.popleft()} got water")
            quantity -= liters
        else:
            print(f"{people.popleft()} must wait")
    usage = input()

print(f"{quantity} liters left")