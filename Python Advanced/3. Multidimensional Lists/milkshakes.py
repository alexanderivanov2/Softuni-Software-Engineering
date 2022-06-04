from collections import deque

chocolate = deque(int(el) for el in input().split(", "))
cup_of_milk = deque(int(el) for el in input().split(", "))
milkshake = 0

while milkshake < 5 and chocolate and cup_of_milk:
    choc, cup = chocolate.pop(), cup_of_milk.popleft()
    if choc <= 0 and cup <= 0:
        continue
    if choc <= 0:
        cup_of_milk.appendleft(cup)
        continue
    if cup <= 0:
        chocolate.append(choc)
        continue
    if choc == cup:
        milkshake += 1
    else:
        cup_of_milk.append(cup)
        chocolate.append(choc - 5)

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(el) for el in chocolate)}")
else:
    print("Chocolate: empty")
if cup_of_milk:
    print(f"Milk: {', '.join(str(el) for el in cup_of_milk)}")
else:
    print("Milk: empty")
