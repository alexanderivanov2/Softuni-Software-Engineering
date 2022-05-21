from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0

while True:
    cup = cups.popleft()
    bottle = bottles.pop()

    if bottle >= cup:
        wasted_water += bottle - cup
    else:
        cup -= bottle
        while cup != 0 and len(bottles) != 0:
            bottle = bottles.pop()
            cup -= bottle
            if cup < 0:
                wasted_water += abs(cup)
                cup = 0

    if len(cups) == 0 or len(bottles) == 0:
        break

if bottles:
    remain = [str(x) for x in bottles]
    print(f"Bottles: {' '.join(remain)}")
else:
    remain = [str(x) for x in cups]
    print(f"Cups: {' '.join(remain)}")

print(f"Wasted litters of water: {wasted_water}")