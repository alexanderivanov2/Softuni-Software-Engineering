def get_kate_start(matrix):
    for row in range(rows):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "k":
                result = [row, col]
                return result


def check_win(kate_place, col_max):
    if kate_place[0] == 0 or kate_place[0] == rows - 1 or kate_place[1] == 0 or kate_place[1] == col_max:
        return True


rows = int(input())
matrix = [[el for el in input()] for i in range(rows)]
col_max = len(matrix[0]) - 1
kate_place = get_kate_start(matrix)
mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}
moves = 0

while True:
    moves += 1
    if check_win(kate_place, col_max):
        print(f"Kate got out in {moves} moves")
        break
    else:
        row = kate_place[0]
        col = kate_place[1]
        if matrix[row - 1][col] == " ":
            matrix[row][col] = "0"
            kate_place[0] -= 1
        elif matrix[row + 1][col] == " ":
            matrix[row][col] = "0"
            kate_place[0] += 1
        elif matrix[row][col - 1] == " ":
            matrix[row][col] = "0"
            kate_place[1] -= 1
        elif matrix[row][col + 1] == " ":
            matrix[row][col] = "0"
            kate_place[1] += 1
        else:
            print("Kate cannot get out")
            break
