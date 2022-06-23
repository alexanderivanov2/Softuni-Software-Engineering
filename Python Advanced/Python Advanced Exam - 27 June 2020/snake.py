def find_snake_and_burrows(matrix):
    row_s, col_s, b1r, b1c, b2r, b2c = 0, 0, 0, 0, 0, 0
    check = True
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "S":
                row_s = row
                col_s = col
            elif matrix[row][col] == "B":
                if check:
                    b1r = row
                    b1c = col
                    check = False
                else:
                    b2r = row
                    b2c = col
    return row_s, col_s, b1r, b1c, b2r, b2c


n = int(input())
matrix = [[el for el in input()] for i in range(n)]
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
row, col, b_r_1, b_c_1, b_r_2, b_c_2 = find_snake_and_burrows(matrix)
win = False
food = 0

while True:
    move = input()
    add_r = moves[move][0]
    add_c = moves[move][1]
    matrix[row][col] = "."
    if row + add_r < 0 or col + add_c < 0 or row + add_r == n or col + add_c == n:
        matrix[row][col] = "."
        win = False
        break
    if matrix[row + add_r][col + add_c] == "B":
        if row + add_r == b_r_1 and col + add_c == b_c_1:
            row = b_r_2
            col = b_c_2
            matrix[b_r_1][b_c_1] = "."
        else:
            row = b_r_1
            col = b_c_1
            matrix[b_r_2][b_c_2] = "."
        matrix[row][col] = "S"
        continue
    row += add_r
    col += add_c
    if matrix[row][col] == "*":
        food += 1
        matrix[row][col] = "S"
    if food == 10:
        win = True
        break

if win:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food}")

for row in matrix:
    print("".join(el for el in row))