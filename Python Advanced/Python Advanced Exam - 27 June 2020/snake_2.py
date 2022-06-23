def create_matrix_find_burrows_and_snake(n):
    matrix = []
    burrow = []
    snake = []
    for i in range(n):
        row = [el for el in input()]
        if "S" in row:
            snake = [i, row.index("S")]
        if "B" in row:
            burrow.append((i, row.index("B")))
        matrix.append(row)
    return matrix, snake, burrow


rows = int(input())
cols = rows
matrix, s, b = create_matrix_find_burrows_and_snake(rows)
food_eaten = 0
in_box = True
r = s[0]
c = s[1]

while food_eaten < 10 and in_box:
    direction = input()
    if direction == "left":
        c -= 1
    elif direction == "right":
        c += 1
    elif direction == "up":
        r -= 1
    elif direction == "down":
        r += 1

    if 0 > r or r >= rows or 0 > c or c >= cols:
        in_box = False
        matrix[s[0]][s[1]] = "."
        break

    if matrix[r][c] == "B":
        if b[0] == (r, c):
            matrix[r][c] = "."
            r = b[1][0]
            c = b[1][1]
        else:
            matrix[r][c] = "."
            r = b[0][0]
            c = b[0][1]
    elif matrix[r][c] == "*":
        food_eaten += 1

    if in_box:
        matrix[s[0]][s[1]] = "."
        s[0] = r
        s[1] = c
        matrix[r][c] = "S"

if in_box:
    print("You won! You fed the snake.")
else:
    print("Game over!")
print(f"Food eaten: {food_eaten}")

for l in matrix:
    print("".join(l))
