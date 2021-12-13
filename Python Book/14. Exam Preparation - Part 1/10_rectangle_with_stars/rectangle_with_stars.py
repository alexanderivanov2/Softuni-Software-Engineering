import math

n = int(input())
procent = "%"
star = "*"
space = " "
top_bottom = n * 2
center = math.ceil(n / 2)
rows = n - 2
if n % 2 == 0:
    range_i = n // 2
else:
    range_i = math.ceil(n / 2)


print(procent * top_bottom)
for row in range(1, range_i):
    print(procent + space * (rows * 2 + 2) + procent)
print(procent + space * rows + star * 2 + space * rows + procent)
for row2 in range(1, range_i):
    print(procent + space * (rows * 2 + 2) + procent)
print(procent * top_bottom)