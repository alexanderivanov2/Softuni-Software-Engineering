n = int(input())

elements = set()

for _ in range(n):
    data = input().split()
    for el in data:
        elements.add(el)

print('\n'.join(elements))