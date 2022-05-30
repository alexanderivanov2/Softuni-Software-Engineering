def create_matrix():
    n = int(input())
    demo_m = []
    for row in range(n):
        column = [int(x) for x in input().split()]
        demo_m.append(column)
    return demo_m


def calculate_primary_diagonal(copy_mat):
    sum_diagonal = 0
    for row in range(len(copy_mat)):
        sum_diagonal += copy_mat[row][row]
    return sum_diagonal


def calculate_secondary_diagonal(copy_mat):
    sum_diagonal2 = 0
    column_index = len(copy_mat)
    for row in range(len(copy_mat)):
        column_index -= 1
        sum_diagonal2 += copy_mat[row][column_index]
    return sum_diagonal2


matrix = create_matrix()
primary_diagonal = calculate_primary_diagonal(matrix)
secondary_diagonal = calculate_secondary_diagonal(matrix)
print(abs(primary_diagonal - secondary_diagonal))
