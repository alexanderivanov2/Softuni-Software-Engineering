from collections import deque


def create_matrix():
    n = int(input())
    demo = []
    for i in range(n):
        elements = [int(x) for x in input().split()]
        demo.append(elements)
    return demo, n


def detonation_bombs(matrix_d, row, column, s):
    move_row = [0, 0, -1, -1, -1, 1, 1, 1]
    move_column = [-1, 1, -1, 0, 1, -1, 0, 1]
    moves = len(move_row)
    for index in range(moves):
        current_row = row + move_row[index]
        current_col = column + move_column[index]
        if 0 <= current_row < s and 0 <= current_col < s:
            if matrix_d[current_row][current_col] > 0:
                matrix_d[current_row][current_col] -= matrix_d[row][column]
    matrix_d[row][column] = 0
    return matrix_d


def calculate_alive_bombs_and_sum(after_bomb_matrix):
    alive = 0
    sums = 0
    for r in after_bomb_matrix:
        for c in r:
            if c > 0:
                alive += 1
                sums += c
    return alive, sums


matrix, size = create_matrix()
bombs = deque([x for x in input().split()])

while bombs:
    current_bomb = bombs.popleft()
    bomb_row, bomb_column = [int(x) for x in current_bomb.split(",")]
    if matrix[bomb_row][bomb_column] > 0:
        matrix = detonation_bombs(matrix, bomb_row, bomb_column, size)

alive_bombs, sum_alive_bombs = calculate_alive_bombs_and_sum(matrix)

print(f"Alive cells: {alive_bombs}")
print(f"Sum: {sum_alive_bombs}")
for row in matrix:
    print(" ".join(str(x) for x in row))