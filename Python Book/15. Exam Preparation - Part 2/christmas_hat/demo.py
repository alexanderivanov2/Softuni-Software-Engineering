n = int(input())
point = "."
star = "*"
line = "-"
width = 4 * n + 1
height = 2 * n + 5
begin_points = (width - 3) // 2
rows = height - 6
print(point * begin_points + "/|\\" + point * begin_points)
print(point * begin_points + "\\|/" + point * begin_points)
print(point * begin_points + star * 3 + point * begin_points)

for row in range(1, rows + 1):
    print(point * (begin_points - row) + star + line * row + star + line * row + star + point * (begin_points - row))

print(star * width)
print(star, end="")

for i in range(1, n * 2 + 1):
    print(point + star, end="")
print()
print(star * width)
