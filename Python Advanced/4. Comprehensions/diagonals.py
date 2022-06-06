def create_matrix(n):
    demo = [[_ for _ in input().split(",")] for _ in range(n)]
    return demo


size = int(input())
matrix = create_matrix(size)
first_diagonal = [int(matrix[i][i]) for i in range(size)]
second_diagonal = [int(matrix[i][size - i - 1]) for i in range(size)]

print(f"First diagonal: {', '.join(str(n) for n in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(str(n) for n in second_diagonal)}. Sum: {sum(second_diagonal)}")
