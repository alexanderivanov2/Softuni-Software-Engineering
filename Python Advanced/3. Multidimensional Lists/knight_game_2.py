def create_matrix(n):
    demo_matrix = []
    for i in range(n):
        l = [el for el in input()]
        demo_matrix.append(l)
    return demo_matrix


def calculate_kills(matrix, r, c):
    killings = 0
    for i in range(len(row_m)):
        if rows > r + row_m[i] >= 0 and columns > c + col_m[i] >= 0 and matrix[r + row_m[i]][c + col_m[i]] == "K":
            killings += 1
    return killings


def get_killer(matrix):
    most_kills = 0
    coordinates = []
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == "K":
                kills = calculate_kills(matrix, r, c)
                if kills > most_kills:
                    coordinates = [r, c]
                    most_kills = kills
    return coordinates


rows = int(input())
row_m = [-2, -2, -1, 1, 2, 2, -1, 1]
col_m = [-1, +1, 2, 2, 1, -1, -2, -2]
matrix = create_matrix(rows)
columns = len(matrix[0])
killer_remove = 0
while True:
    killer_coordinates = get_killer(matrix)
    if killer_coordinates:
        matrix[killer_coordinates[0]][killer_coordinates[1]] = "0"
        killer_remove += 1
    else:
        break

print(killer_remove)