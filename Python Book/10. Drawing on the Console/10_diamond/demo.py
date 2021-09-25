n = int(input())

line = "-"
middle_line = 1
star = "*"
rows = 0

if n % 2 == 0:
    rows = (n - 2) // 2
    middle_line += 1
    n1 = n - 1
else:
    rows = (n - 1) // 2
    n1 = n
print(line * rows, end="")
if not n % 2 == 0:
    print(star, end="")
else:
    print(star * 2, end="")
print(line * rows)

for top_rows in range(2, rows + 1):
    print(line * (n1 - (top_rows + rows)), end="")
    print(star, end="")
    print(line * middle_line, end="")
    print(star, end="")
    print(line * (n1 - (top_rows + rows)))
    middle_line += 2

if n < 3:
    print("", end="")
else:
    print(star + (line * (n - 2)) + star)

for down_rows in range(1, rows):
    if n < 3:
        print("", end="")
    else:
        print(line * down_rows, end="")
        print(star + (line * (n - 4)) + star, end="")
        print(line * down_rows)
        n -= 2

if n < 3:
    print("",end="")
else:
    print(line * rows, end="")
    if n % 2 == 0:
        print(star * 2, end="")
    else:
        print(star, end="")
print(line * rows)
