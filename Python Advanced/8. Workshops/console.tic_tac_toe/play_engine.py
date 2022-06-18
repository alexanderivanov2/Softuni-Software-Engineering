from tic_tac_toe import setup
from tic_tac_toe.helper import possitions_mapper


def is_position_valid(pos):
    if pos in [str(el) for el in range(1, 10)]:
        return True
    return False


def position_available(board, position):
    row, col = possitions_mapper[position]
    current_element = board[row][col]
    if not current_element == " ":
        return False
    return True


def draw_board(board):
    print()
    print(f"{setup.player_names[0]} - {setup.player_signs[0]}")
    print(f"{setup.player_names[1]} - {setup.player_signs[1]}")
    print("-" * 13 + " " * 5 + "-" * 13)
    start = 1
    end = 4
    for row in range(len(board)):
        print("|", end=" ")
        print(" | ".join(board[row]), end=" ")
        print("|" + " " * 5, end="")
        print("|", end=" ")
        print(" | ".join(str(el) for el in range(start, end)), end=" ")
        print("|" + " " * 5)
        print("-" * 13 + " " * 5 + "-" * 13)
        start += 3
        end += 3


def play_turn(board, sign, position):
    if position_available(board, position):
        row, col = possitions_mapper[position]
        board[row][col] = sign
        draw_board(board)
    else:
        current_position = input(f"select a valid available position from 1-9: ")
        current_position = int(current_position)
        play_turn(board, sign, current_position)


def is_row_winner():
    for row_number in range(len(setup.board)):
        if setup.board[row_number].count("X") == 3 or setup.board[row_number].count("O") == 3:
            return True
    return False


def is_col_winner():
    x = 0
    o = 0
    for col in range(3):
        x = 0
        o = 0
        for row in range(3):
            if setup.board[row][col] == "X":
                x += 1
            elif setup.board[row][col] == "O":
                o += 1
        if x == 3 or o == 3:
            return True
    return False


def is_right_diagonal_winner():
    x = 0
    o = 0
    row = 0
    for col in range(2, -1, -1):
        if setup.board[row][col] == "X":
            x += 1
        elif setup.board[row][col] == "O":
            o += 1
        row += 1
    if x == 3 or o == 3:
        return True
    return False


def is_left_diagonal_winner():
    x = 0
    o = 0
    for row in range(3):
        if setup.board[row][row] == "X":
            x += 1
        elif setup.board[row][row] == "O":
            o += 1
    if x == 3 or o == 3:
        return True
    return False


def has_won():
    if is_row_winner() or is_col_winner() or is_right_diagonal_winner() or is_left_diagonal_winner():
        return True
    return False


def has_moves(counter):
    if counter < 10:
        return True
    return False


def check_selected_position_is_valid(position, counter):
    if not position.isdigit() or not is_position_valid(position):
        position = input(f"{setup.player_names[counter % 2]}, select position from 1-9: ")
        return check_selected_position_is_valid(position, counter)
    return position



def play():
    turns_counter = 1
    while not has_won() and has_moves(turns_counter):
        current_position = input(f"{setup.player_names[turns_counter % 2]}, select position from 1-9: ")
        current_position = check_selected_position_is_valid(current_position, turns_counter)
        current_position = int(current_position)
        play_turn(setup.board, setup.player_signs[turns_counter % 2], current_position)
        turns_counter += 1

    if not has_moves(turns_counter) and not has_won():
        print("Draw!")
        return
    turns_counter -= 1
    print(f"{setup.player_names[turns_counter % 2]} won!")

