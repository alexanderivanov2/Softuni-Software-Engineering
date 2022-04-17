def create_matrix(n_for_rows):
    matrix_create = [[int(el) for el in input().split()] for row in range(n)]
    return matrix_create


def do_attack(matrix, row, col):
    destroy = 0
    ship = matrix[row][col]
    if ship == 0:
        return matrix, destroy
    elif ship == 1:
        destroy += 1
    matrix[row][col] -= 1
    return matrix, destroy


n = int(input())
matrix = create_matrix(n)
text_attacks = input().split()
text_attacks = [el.split("-") for el in text_attacks]
attacks = [[int(el) for el in line] for line in text_attacks]
count = 0

for attack in attacks:
    row = attack[0]
    col = attack[1]
    matrix, destroyed = do_attack(matrix, row, col)
    count += destroyed

print(count)
