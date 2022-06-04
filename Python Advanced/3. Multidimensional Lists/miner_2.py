from collections import deque


def create_matrix(n):
    demo_matrix = []
    coal = 0
    s_index = []
    for i in range(n):
        line = [el for el in input().split()]
        if "c" in line:
            coal += line.count("c")
        if "s" in line:
            s_index = [i, line.index("s")]
        demo_matrix.append(line)
    return demo_matrix, coal, s_index, len(demo_matrix[0])


direction = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
rows = int(input())
directions = deque(el for el in input().split())
matrix, coals, current_point, columns = create_matrix(rows)
game_over = False

while directions and coals > 0:
    direct = directions.popleft()
    indexes = direction[direct]
    row = current_point[0] + indexes[0]
    col = current_point[1] + indexes[1]
    if rows> row >= 0 and columns > col >= 0:
        if matrix[row][col] == "e":
            game_over = True
        elif matrix[row][col] == "c":
            coals -= 1
            matrix[row][col] = "s"
    else:
        continue
    matrix[current_point[0]][current_point[1]] = "*"
    current_point[0] = row
    current_point[1] = col
    if game_over:
        break

if game_over:
    print(f"Game over! ({current_point[0]}, {current_point[1]})")
elif coals > 0:
    print(f"{coals} pieces of coal left. ({current_point[0]}, {current_point[1]})")
else:
    print(f"You collected all coal! ({current_point[0]}, {current_point[1]})")