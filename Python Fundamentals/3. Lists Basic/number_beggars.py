beggars = [int(el) for el in input().split(", ")]
n = int(input())
result = []

for _ in range(n):
    sum = 0
    for i in range(_, len(beggars), n):
        sum += beggars[i]
    result.append(sum)

print(result)