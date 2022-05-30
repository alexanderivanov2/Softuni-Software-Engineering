# size = int(input())
# matrix = []
# for _ in range(size):
#     matrix.append(input().split())
#
# best_result, best_route, best_direction = float('-inf'), [], ""
#
# for r in range(size):
#     for c in range(size):
#         if matrix[r][c] == "B":
#             bunny_is_here = [r, c]
#
# cur_row, cur_col = bunny_is_here
# current_result, current_route = 0, []
# # TRY UP
# while cur_row > 0:
#     cur_row -= 1
#     if matrix[cur_row][cur_col] == "X":
#         break
#     current_result += int(matrix[cur_row][cur_col])
#     current_route.append([cur_row, cur_col])
#     if current_result > best_result:
#         best_result = current_result
#         best_route = current_route
#         best_direction = "up"
#
# cur_row, cur_col = bunny_is_here
# current_result, current_route = 0, []
# # TRY DOWN
# while cur_row < size - 1:
#     cur_row += 1
#     if matrix[cur_row][cur_col] == "X":
#         break
#     current_result += int(matrix[cur_row][cur_col])
#     current_route.append([cur_row, cur_col])
#     if current_result > best_result:
#         best_result = current_result
#         best_route = current_route
#         best_direction = "down"
#
# cur_row, cur_col = bunny_is_here
# current_result, current_route = 0, []
# # TRY LEFT
# while cur_col > 0:
#     cur_col -= 1
#     if matrix[cur_row][cur_col] == "X":
#         break
#     current_result += int(matrix[cur_row][cur_col])
#     current_route.append([cur_row, cur_col])
#     if current_result > best_result:
#         best_result = current_result
#         best_route = current_route
#         best_direction = "left"
#
# cur_row, cur_col = bunny_is_here
# current_result, current_route = 0, []
# # TRY RIGHT
# while cur_col < size - 1:
#     cur_col += 1
#     if matrix[cur_row][cur_col] == "X":
#         break
#     current_result += int(matrix[cur_row][cur_col])
#     current_route.append([cur_row, cur_col])
#     if current_result > best_result:
#         best_result = current_result
#         best_route = current_route
#         best_direction = "right"
#
# print(best_direction)
# for row in best_route:
#     print(row)
# print(best_result)
size = int(input())
matrix = []
for row in range(size):
    column = input().split()
    matrix.append(column)
    if "B" in column:
        bunny_is_here = [row, column.index("B")]
# The infinity condition was quite dodgy and unfair, fails if starting from zero,
# i.e. tests with negative numbers are carried out
best_result, best_direction, best_route = float('-inf'), "", []

current_result = 0
current_route = []
try_again = bunny_is_here
# LEFT
while bunny_is_here[1] > 0:
    bunny_is_here = [bunny_is_here[0], bunny_is_here[1] - 1]
    y, x = bunny_is_here[0], bunny_is_here[1]
    if matrix[y][x] == "X":
        break
    current_result += int(matrix[y][x])
    current_route.append(bunny_is_here)
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "left"

current_result = 0
current_route = []
bunny_is_here = try_again
# RIGHT
while bunny_is_here[1] < size - 1:
    bunny_is_here = [bunny_is_here[0], bunny_is_here[1] + 1]
    y, x = bunny_is_here[0], bunny_is_here[1]
    if matrix[y][x] == "X":
        break
    current_result += int(matrix[y][x])
    current_route.append(bunny_is_here)
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "right"

current_result = 0
current_route = []
bunny_is_here = try_again
# UP
while bunny_is_here[0] > 0:
    bunny_is_here = [bunny_is_here[0] - 1, bunny_is_here[1]]
    y, x = bunny_is_here[0], bunny_is_here[1]
    if matrix[y][x] == "X":
        break
    current_result += int(matrix[y][x])
    current_route.append(bunny_is_here)
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "up"

current_result = 0
current_route = []
bunny_is_here = try_again
# DOWN
while bunny_is_here[0] < size - 1:
    bunny_is_here = [bunny_is_here[0] + 1, bunny_is_here[1]]
    y, x = bunny_is_here[0], bunny_is_here[1]
    if matrix[y][x] == "X":
        break
    current_result += int(matrix[y][x])
    current_route.append(bunny_is_here)
    if current_result > best_result:
        best_result = current_result
        best_route = current_route
        best_direction = "down"

print(best_direction)
print(*best_route, sep="\n")
print(best_result)
