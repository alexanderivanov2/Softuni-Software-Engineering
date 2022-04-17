def get_kate_start(matrix):
    for row in range(rows):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "k":
                result = [row, col]
                return result


def check_win(kate_place, col_max):
    if kate_place[0] == 0 or kate_place[0] == rows - 1 or kate_place[1] == 0 or kate_place[1] == col_max:
        return True


def result(kate_place, col_max, moves, res=True):
    if check_win(kate_place, col_max):
        res = True
        moves += 1
        return res, moves
    row = kate_place[0]
    col = kate_place[1]
    if matrix[row - 1][col] == " ":
        matrix[row][col] = "0"
        kate_place[0] -= 1
        moves += 1
        result(kate_place, col_max, moves)
        if res:
            return res, moves

    if matrix[row][col + 1] == " ":
        matrix[row][col] = "0"
        kate_place[1] += 1
        moves += 1
        result(kate_place, col_max, moves)
        if res:
            return res, moves

    if matrix[row + 1][col] == " ":
        matrix[row][col] = "0"
        kate_place[0] += 1
        moves += 1
        result(kate_place, col_max, moves)
        if res:
            return res, moves
    if matrix[row][col - 1] == " ":
        matrix[row][col] = "0"
        kate_place[1] -= 1
        moves += 1
        result(kate_place, col_max, moves)
        if res:
            return res, moves

    moves -= 1
    res = False
    return res, moves


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

results, moves = result(kate_place, col_max, moves)

print(moves)
if results:
    print("Yes")
else:
    print("No")
