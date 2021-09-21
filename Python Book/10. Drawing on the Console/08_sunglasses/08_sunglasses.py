import math

n = int(input())
middle_row = math.ceil((n - 2) / 2)
up_down = "*" * (n * 2)
middle = "/" * (n + (n - 2))
middle2 = " " * n
middle4 = "|" * n

print(up_down, end="")
print(middle2, end="")
print(up_down)

for row in range(1, n - 2 + 1):
    print("*" + middle + "*", end="")
    if n == (n % 2 == 0) and row == 0:
        print(middle4, end="")
    elif row != middle_row:
        print(middle2, end="")
    else:
        print(middle4, end="")
    print("*" + middle + "*")


print(up_down, end="")
print(middle2, end="")
print(up_down, end="")
