a = int(input())
b = int(input())

while b != 0:
    oldB = b
    b = a % b
    a = oldB

print(a)