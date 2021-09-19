n = int(input())

print(" " * (n + 1) + "|")
for row in range(1, n + 1):
    space = n - row
    stars = row