n = int(input())

print("+", end=" ")
print(("-" + " ") * (n - 2), end="")
print("+")

for cow in range(n-2):
    print("|", end=" ")
    print(("-" + " ") * (n - 2), end="")
    print("|", end=" ")
    print()

print("+", end=" ")
print(("-" + " ") * (n - 2), end="")
print("+")