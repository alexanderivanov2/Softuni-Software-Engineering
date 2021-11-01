n = int(input())
n0 = 1
n1 = 1

for i in range(0, n - 1):
    n_next = n1 + n0
    n0 = n1
    n1 = n_next

print(n1)