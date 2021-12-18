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