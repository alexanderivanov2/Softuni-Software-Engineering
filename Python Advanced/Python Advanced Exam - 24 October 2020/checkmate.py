def found_king(chess_board):
    for row in range(8):
        for col in range(8):
            if chess_board[row][col] == "K":
                return row, col


def search_right_up_diagonal(chess_board, row2, col2):
    while True:
        row2 += search_sides["right_up_diagonal"][0]
        col2 += search_sides["right_up_diagonal"][1]
        if row2 < 0 or col2 == 8:
            return
        if chess_board[row2][col2] == "Q":
            return [row2, col2]


def search_right(chess_board, row2, col2):
    while True:
        row2 += search_sides["right"][0]
        col2 += search_sides["right"][1]
        if col2 == 8:
            return
        if chess_board[row2][col2] == "Q":
            return [row2, col2]


def search_right_down_diagonal(chess_board, row2, col2):
    while True:
        row2 += search_sides["right_down_diagonal"][0]
        col2 += search_sides["right_down_diagonal"][1]
        if col2 == 8 or row2 == 8:
            return
        if chess_board[row2][col2] == "Q":
            return [row2, col2]


def search_down(chess_board, row2, col2):
    while True:
        row2 += search_sides["down"][0]
        col2 += search_sides["down"][1]
        if row2 == 8:
            return
        if chess_board[row2][col2] == "Q":
            return [row2, col2]


def search_left_down_diagonal(chess_board, row2, col2):
    while True:
        row2 += search_sides["left_down_diagonal"][0]
        col2 += search_sides["left_down_diagonal"][1]
        if row2 == 8 or col2 < 0:
            return
        if chess_board[row2][col2] == "Q":
            return [row2, col2]


def left(chess_board, row2, col2):
    while True:
        row2 += search_sides["left"][0]
        col2 += search_sides["left"][1]
        if col2 < 0:
            return
        if chess_board[row2][col2] == "Q":
            return [row2, col2]


def left_up_diagonal(chess_board, row2, col2):
    while True:
        row2 += search_sides["left_up_diagonal"][0]
        col2 += search_sides["left_up_diagonal"][1]
        if col2 < 0 or row2 < 0:
            return
        if chess_board[row2][col2] == "Q":
            return [row2, col2]


def up(chess_board, row2, col2):
    while True:
        row2 += search_sides["up"][0]
        col2 += search_sides["up"][1]
        if row2 < 0:
            return
        if chess_board[row2][col2] == "Q":
            return [row2, col2]


chess_board = [[square for square in input().split()] for i in range(8)]
row, col = found_king(chess_board)
search_sides = {
    "right_up_diagonal": (-1, 1),
    "right": (0, 1),
    "right_down_diagonal": (1, 1),
    "down": (1, 0),
    "left_down_diagonal": (1, -1),
    "left": (0, -1),
    "left_up_diagonal": (-1, -1),
    "up": (-1, 0)
}

captures = []
captures.append(search_right_up_diagonal(chess_board, row, col))
captures.append(search_right(chess_board, row, col))
captures.append(search_right_down_diagonal(chess_board, row, col))
captures.append(search_down(chess_board, row, col))
captures.append(search_left_down_diagonal(chess_board, row, col))
captures.append(left(chess_board, row, col))
captures.append(left_up_diagonal(chess_board, row, col))
captures.append(up(chess_board, row, col))

captures = [capture for capture in captures if capture is not None]

if captures:
    print("\n".join([str(el) for el in captures]))
else:
    print("The king is safe!")
