def check_cordinate(matrix, row, col):
    return matrix[row][col]


players = {}
player_1, player_2 = input().split(", ")
players[player_1] = {"points": 501, "throws": 0}
players[player_2] = {"points": 501, "throws": 0}
matrix = [[col_el for col_el in input().split()] for i in range(7)]
current_player = player_1

while True:
    players[current_player]["throws"] += 1
    row, col = [int(cordinate) for cordinate in input()[1:-1].split(", ") if cordinate.isdigit()]
    row = int(row)
    col = int(col)
    if not (0 <= row < 7 and 0 <= col < 7):
        current_player = player_2 if current_player == player_1 else player_1
        continue
    symbol = check_cordinate(matrix, row, col)

    if symbol == "B":
        break
    elif symbol == "D":
        points = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 2
        players[current_player]["points"] -= points
    elif symbol == "T":
        points = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 3
        players[current_player]['points'] -= points
    else:
        players[current_player]["points"] -= int(matrix[row][col])

    if players[current_player]["points"] <= 0:
        break
    current_player = player_2 if current_player == player_1 else player_1

print(f"{current_player} won the game with {players[current_player]['throws']} throws!")
