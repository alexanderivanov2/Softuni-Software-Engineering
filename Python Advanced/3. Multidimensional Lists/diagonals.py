def create_matrix(n):
    demo_matrix = []
    for i in range(n):
        row = [int(el) for el in input().split(",")]
        demo_matrix.append(row)
    return demo_matrix


def calculate_primary_diagonal(matrix, n):
    diagonal = []
    for i in range(n):
        diagonal.append(matrix[i][i])
    print(f"Primary diagonal: {', '.join(str(el) for el in diagonal)}. Sum: {sum(diagonal)}")


def calculate_secondary_diagonal(matrix, n):
    diagonal = []
    for i in range(n):
        diagonal.append(matrix[i][n - i - 1])
    print(f"Secondary diagonal: {', '.join(str(el) for el in diagonal)}. Sum: {sum(diagonal)}")


n = int(input())
matrix = create_matrix(n)
calculate_primary_diagonal(matrix, n)
calculate_secondary_diagonal(matrix, n)
