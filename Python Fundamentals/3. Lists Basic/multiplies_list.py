factor = int(input())
n = int(input())
multiples_list = []

for i in range(1, n + 1):
    multiples_list.append(i * factor)

print(multiples_list)
