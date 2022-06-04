from collections import deque


def get_moves():
    get_move = deque([x for x in input().split()])
    return get_move


def create_matrix(n):
    demo = []
    for _ in range(n):
        elements = [x for x in input().split()]
        demo.append(elements)
    return demo


def find_start(search_matrix):
    for r in range(len(search_matrix)):
        if "s" in search_matrix[r]:
            c = search_matrix[r].index("s")
            return r, c


def print_result(final_matrix, cordinat):
    all_coals = 0
    for row in final_matrix:
        if "c" in row:
            all_coals += row.count("c")
    if all_coals == 0:
        print(f"You collected all coals! {cordinat}")
    else:
        print(f"{all_coals} coals left. {cordinat}")


size = int(input())
moves = get_moves()
matrix = create_matrix(size)
directions = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}
start_r, start_c = find_start(matrix)

while moves:
    direction = moves.popleft()
    if 0 <= start_r + directions[direction][0] < size and 0 <= start_c + directions[direction][1] < size:
        start_r += directions[direction][0]
        start_c += directions[direction][1]
        el = matrix[start_r][start_c]
        if el == "c":
            matrix[start_r][start_c] = "*"
        elif el == "e":
            print(f"Game over! ({start_r}, {start_c})")
            break
    if len(moves) == 0:
        final_cordinates = (start_r, start_c)
        print_result(matrix, final_cordinates)
