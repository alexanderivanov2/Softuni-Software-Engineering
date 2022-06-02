from collections import deque


def subtract(n1, n2):
    res = abs(n1 - n2)
    return res


def add(n1, n2):
    res = abs(n1 + n2)
    return res


def multiply(n1, n2):
    res = abs(n1 * n2)
    return res


def divide(n1, n2):
    res = 0
    if not n2 == 0:
        res = abs(n1 / n2)
    return res


working_bees = deque(int(el) for el in input().split())
nectar = [int(el) for el in input().split()]
symbols = deque(el for el in input().split())
total_honey = 0

while working_bees and nectar:
    bee = working_bees[0]
    nec = nectar.pop()
    if nec >= bee:
        bee = working_bees.popleft()
        symbol = symbols.popleft()
        if symbol == "-":
            total_honey += subtract(bee, nec)
        elif symbol == "+":
            total_honey += add(bee, nec)
        elif symbol == "*":
            total_honey += multiply(bee, nec)
        elif symbol == "/":
            total_honey += divide(bee, nec)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(el) for el in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(el) for el in nectar)}")
