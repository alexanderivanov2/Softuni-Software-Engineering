def create_matrix():
    rows_size = int(input())
    demo = []
    for row in range(rows_size):
        elements = [x for x in input()]
        demo.append(elements)
    return demo, rows_size


def kills_counter(matrix_copy, r2, c2):
    count_kills = 0
    rows_moves = [-1, 1, -2, -2, 1, -1, 2, 2]
    column_moves = [-2, -2, -1, 1, 2, 2, -1, 1]
    size = len(matrix_copy)

    for r_index in range(len(rows_moves)):
        check_row = r2 + rows_moves[r_index]
        check_column = c2 + column_moves[r_index]
        if 0 <= check_row < size and 0 <= check_column < size:
            if matrix_copy[check_row][check_column] == "K":
                count_kills += 1
    return count_kills


def get_best_horse(copy_m, rows2):
    most_kills = 0
    horse = []
    for r in range(rows2):
        for c in range(rows2):
            if copy_m[r][c] == "K":
                kills = kills_counter(copy_m, r, c)
                if kills > most_kills:
                    most_kills = kills
                    horse = [r, c]
    return horse


matrix, rows = create_matrix()
counter = 0

while True:
    result = get_best_horse(matrix, rows)
    if result:
        matrix[result[0]][result[1]] = "0"
    else:
        print(counter)
        break
    counter += 1

