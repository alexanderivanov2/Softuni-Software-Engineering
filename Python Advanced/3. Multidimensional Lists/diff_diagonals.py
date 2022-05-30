def create_matrix(n):
    demo_matrix = []
    for i in range(n):
        row = [int(el) for el in input().split()]
        demo_matrix.append(row)
    return demo_matrix


def calculate_primary_diagonal(matrix, n):
    diagonal = []
    for i in range(n):
        diagonal.append(matrix[i][i])
    return sum(diagonal)


def calculate_secondary_diagonal(matrix, n):
    diagonal = []
    for i in range(n):
        diagonal.append(matrix[i][n - i - 1])
    return sum(diagonal)


n = int(input())
matrix = create_matrix(n)
primary = calculate_primary_diagonal(matrix, n)
secondary = calculate_secondary_diagonal(matrix, n)
print(abs(primary - secondary))