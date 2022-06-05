def create_matrix(n):
    demo_matrix = []
    player_position = [0, 0]
    for i in range(n):
        line = [el for el in input()]
        if "P" in line:
            player_position = [i, line.index("P")]
        demo_matrix.append(line)
    return demo_matrix, player_position


directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
rows, cows = [int(el) for el in input().split()]
matrix, current_position = create_matrix(rows)
direction = [el for el in input()]
win = False
get_you = False

while not win and not get_you:
    make_it_b = []
    d = directions[direction.pop(0)]
    row = current_position[0] + d[0]
    col = current_position[1] + d[1]
    if rows > row >= 0 and cows > col >= 0:
        if matrix[row][col] == ".":
            matrix[row][col] = "P"
            matrix[current_position[0]][current_position[1]] = "."
        elif matrix[row][col] == "B":
            get_you = True

        current_position[0] = row
        current_position[1] = col
    else:
        win = True
        matrix[current_position[0]][current_position[1]] = "."
    for r in range(rows):
        for c in range(cows):
            if matrix[r][c] == "B":
                # up
                if rows > r - 1 >= 0 and cows > c >= 0 and (r - 1, c) not in make_it_b:
                    if matrix[r - 1][c] == "P":
                        get_you = True
                    make_it_b.append((r - 1, c))
                # down
                if rows > r + 1 >= 0 and cows > c >= 0 and (r + 1, c) not in make_it_b:
                    if matrix[r + 1][c] == "P":
                        get_you = True
                    make_it_b.append((r + 1, c))
                # left
                if rows > r >= 0 and cows > c - 1 >= 0 and (r, c - 1) not in make_it_b:
                    if matrix[r][c - 1] == "P":
                        get_you = True
                    make_it_b.append((r, c - 1))
                # right
                if rows > r >= 0 and cows > c + 1 >= 0 and (r, c + 1) not in make_it_b:
                    if matrix[r][c + 1] == "P":
                        get_you = True
                    make_it_b.append((r, c + 1))
    for indexes in make_it_b:
        matrix[indexes[0]][indexes[1]] = "B"

for l in matrix:
    print("".join(l))

if get_you:
    print(f"dead: {current_position[0]} {current_position[1]}")
else:
    print(f"won: {current_position[0]} {current_position[1]}")