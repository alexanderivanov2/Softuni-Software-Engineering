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
