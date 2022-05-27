from collections import deque


def create_matrix(n):
    demo_matrix = []
    for i in range(n):
        line = [int(el) for el in input().split()]
        demo_matrix.append(line)
    return demo_matrix


rows = int(input())
matrix = create_matrix(rows)
columns = len(matrix[0])
coordinates = deque([[int(a) for a in el.split(",")] for el in input().split()])

while coordinates:
    coordinate = coordinates.popleft()
    r = coordinate[0]
    c = coordinate[1]
    if matrix[r][c] <= 0:
        continue
    # Up left
    if rows > r - 1 >= 0 and columns > c - 1 >= 0 and matrix[r - 1][c - 1] > 0:
        matrix[r - 1][c - 1] -= matrix[r][c]
    # up
    if rows > r - 1 >= 0 and columns > c >= 0 and matrix[r - 1][c] > 0:
        matrix[r - 1][c] -= matrix[r][c]
    # up right
    if r - 1 >= 0 and 0 <= c + 1 < columns and matrix[r - 1][c + 1] > 0:
        matrix[r - 1][c + 1] -= matrix[r][c]
    # left
    if rows > r >= 0 and columns > c - 1 >= 0 and matrix[r][c - 1] > 0:
        matrix[r][c - 1] -= matrix[r][c]
    # right
    if rows > r >= 0 and columns > c + 1 >= 0 and matrix[r][c + 1] > 0:
        matrix[r][c + 1] -= matrix[r][c]
    # down left
    if rows > r + 1 >= 0 and columns > c - 1 >= 0 and matrix[r + 1][c - 1] > 0:
        matrix[r + 1][c - 1] -= matrix[r][c]
    # down
    if rows > r + 1 >= 0 and columns > c >= 0 and matrix[r + 1][c] > 0:
        matrix[r + 1][c] -= matrix[r][c]
    # down right
    if rows > r + 1 >= 0 and columns > c + 1 >= 0 and matrix[r + 1][c + 1]:
        matrix[r + 1][c + 1] -= matrix[r][c]
    matrix[r][c] = 0

all_alive_cells = []
cells = [[all_alive_cells.append(a) for a in el if a > 0] for el in matrix]

print(f"Alive cells: {len(all_alive_cells)}")
print(f"Sum: {sum(all_alive_cells)}")
[print(' '.join(str(el) for el in l)) for l in matrix]