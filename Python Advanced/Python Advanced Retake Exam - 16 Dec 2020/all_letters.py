def find_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "P":
                return row, col


letter = input()
n = int(input())
matrix = [[el for el in input()] for i in range(n)]
m = int(input())

sides = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, col = find_player(matrix)
matrix[row][col] = '-'

for i in range(m):
    side = input()
    add_r = sides[side][0]
    add_c = sides[side][1]
    if row + add_r == n or row + add_r < 0 or col + add_c < 0 or col + add_c == n:
        if len(letter) > 0:
            letter = letter[:-1]
            continue
    row += add_r
    col += add_c
    if matrix[row][col] == "-":
        continue
    else:
        letter += matrix[row][col]
        matrix[row][col] = "-"

matrix[row][col] = "P"
print(letter)
for row in matrix:
    print("".join(row))