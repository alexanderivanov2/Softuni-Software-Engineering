def create_matrix_and_get_b_index():
    matrix = []
    bullseye = None
    for i in range(7):
        row = [el for el in input().split()]
        if "B" in row:
            bullseye = (i, row.index("B"))
        matrix.append(row)
    return matrix, bullseye


name_1, name_2 = input().split(",")
p1 = {"name": name_1, "points": 501, "throws": 0, "win": False}
p2 = {"name": name_2, "points": 501, "throws": 0, "win": False}
matrix, bullseye = create_matrix_and_get_b_index()
current_player = p1

while not p1["win"] and not p2["win"]:
    coordinates = input()
    row, col = coordinates[1:-1].split(",")
    row = int(row)
    col = int(col)
    if 0 <= row < 7 and 0 <= col <= 6:
        if row == bullseye[0] and col == bullseye[1]:
            current_player["win"] = True
        elif matrix[row][col] == "D":
            score = int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])
            current_player["points"] -= score * 2
            if current_player["points"] <= 0:
                current_player["win"] = True
        elif matrix[row][col] == "T":
            score = int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])
            current_player["points"] -= score * 3
            if current_player["points"] <= 0:
                current_player["win"] = True
        else:
            current_player["points"] -= int(matrix[row][col])
            if current_player["points"] <= 0:
                current_player["win"] = True

    current_player["throws"] += 1
    current_player = p2 if current_player == p1 else p1


if p1["win"]:
    print(f"{p1['name']} won the game with {p1['throws']} throws!")
else:
    print(f"{p2['name']} won the game with {p2['throws']} throws!")