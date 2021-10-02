n = int(input())

points, grid = ".", "#"
before_mid_outside_points = (n - 1) // 2
before_mid_inside_points = n - 2
mid_grid = before_mid_outside_points + 1
points_after_mid = 0
width = before_mid_outside_points * 2 + n

print(points * before_mid_outside_points + grid * n + points * before_mid_outside_points)

for row in range(1, n - 1):
    print(points * before_mid_outside_points + grid + points * before_mid_inside_points + grid
          + points * before_mid_outside_points)

print(grid * mid_grid + points * before_mid_inside_points + grid * mid_grid)

for row2 in range(1, n - 1):
    points_after_mid = width - row2 * 2 - 2
    print(points * row2 + grid + points * points_after_mid + grid + points * row2)

print(points * (n - 1) + grid + points * (n - 1))