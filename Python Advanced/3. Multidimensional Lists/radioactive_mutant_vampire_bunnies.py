from collections import deque


def create_matrix():
    demo = []
    n_rows, m_col = [int(x) for x in input().split()]
    for _ in range(n_rows):
        elements = [x for x in input()]
        demo.append(elements)
    return demo, n_rows, m_col


def find_p_index(cop_m, rows, columns):
    for i in range(rows):
        for i2 in range(columns):
            if "P" == cop_m[i][i2]:
                return i, i2


def player_move(copy_m, statute, statute2, move, moves, i_r, i_c, side_r, side_c):
    copy_m[i_r][i_c] = "."
    m_r = i_r + moves[move][0]
    m_c = i_c + moves[move][1]
    if 0 <= m_r < side_r and 0 <= m_c < side_c:
        if copy_m[m_r][m_c] == ".":
            copy_m[m_r][m_c] = "P"
        elif copy_m[m_r][m_c] == "B":
            statute = True
        i_r = m_r
        i_c = m_c
    else:
        statute2 = True
    return copy_m, statute, statute2, i_r, i_c


def bunny_multiply(matrix_b, statute_catch, col_s):
    for r in range(len(matrix_b)):
        for c in range(col_s):
            if matrix_b[r][c] == "B":
                matrix_b, statute_catch = multiply_current_bunny(matrix_b, statute_catch, r, c, col_s)
                # if statute_catch:
                #     return matrix_b, statute_catch
    matrix_b = b_become_big(matrix_b, col_s)
    return matrix_b, statute_catch


def multiply_current_bunny(mat_b, stat_catch, b_r, b_c, s_col):
    ending_r = len(mat_b)
    dict_turn = {"l": (b_r, b_c - 1), "r": (b_r, b_c + 1), "u": (b_r - 1, b_c), "d": (b_r + 1, b_c)}
    if 0 <= dict_turn["l"][0] < ending_r and 0 <= dict_turn["l"][1] < s_col:
        if mat_b[dict_turn["l"][0]][dict_turn["l"][1]] == ".":
            mat_b[dict_turn["l"][0]][dict_turn["l"][1]] = "b"
        elif mat_b[dict_turn["l"][0]][dict_turn["l"][1]] == "P":
            mat_b[dict_turn["l"][0]][dict_turn["l"][1]] = "b"
            stat_catch = True
    if 0 <= dict_turn["r"][0] < ending_r and 0 <= dict_turn["r"][1] < s_col:
        if mat_b[dict_turn["r"][0]][dict_turn["r"][1]] == ".":
            mat_b[dict_turn["r"][0]][dict_turn["r"][1]] = "b"
        elif mat_b[dict_turn["r"][0]][dict_turn["r"][1]] == "P":
            mat_b[dict_turn["r"][0]][dict_turn["r"][1]] = "b"
            stat_catch = True
    if 0 <= dict_turn["u"][0] < ending_r and 0 <= dict_turn["u"][1] < s_col:
        if mat_b[dict_turn["u"][0]][dict_turn["u"][1]] == ".":
            mat_b[dict_turn["u"][0]][dict_turn["u"][1]] = "b"
        elif mat_b[dict_turn["u"][0]][dict_turn["u"][1]] == "P":
            mat_b[dict_turn["u"][0]][dict_turn["u"][1]] = "b"
            stat_catch = True
    if 0 <= dict_turn["d"][0] < ending_r and 0 <= dict_turn["d"][1] < s_col:
        if mat_b[dict_turn["d"][0]][dict_turn["d"][1]] == ".":
            mat_b[dict_turn["d"][0]][dict_turn["d"][1]] = "b"
        elif mat_b[dict_turn["d"][0]][dict_turn["d"][1]] == "P":
            mat_b[dict_turn["d"][0]][dict_turn["d"][1]] = "b"
            stat_catch = True
    return mat_b, stat_catch


def b_become_big(mat_copy2, col_sizes):
    for r2 in range(len(mat_copy2)):
        for c2 in range(col_sizes):
            if mat_copy2[r2][c2] == "b":
                mat_copy2[r2][c2] = "B"
    return mat_copy2


def print_result(final_matrix):
    for current_row in final_matrix:
        print("".join(current_row))


matrix, row_size, col_size = create_matrix()
turns = deque([x for x in input()])
turn = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
catch_p = False
exit_p = False
index_r, index_c = find_p_index(matrix, row_size, col_size)

while True:
    if catch_p:
        print_result(matrix)
        print(f"dead: {index_r} {index_c}")
        break
    elif exit_p:
        print_result(matrix)
        print(f"won: {index_r} {index_c}")
        break
    t = turns.popleft()
    matrix, catch_p, exit_p, index_r, index_c = player_move(matrix, catch_p, exit_p, t, turn, index_r, index_c,
                                                            row_size, col_size)
    matrix, catch_p = bunny_multiply(matrix, catch_p, col_size)
    matrix = b_become_big(matrix, col_size)
