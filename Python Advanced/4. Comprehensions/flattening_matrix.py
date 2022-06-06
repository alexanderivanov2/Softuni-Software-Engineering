size = int(input())
matrix = [[j for j in row] for row in input().split(", ")]

flattering_matrix = [int(num) for sublist in matrix for num in sublist]
print(flattering_matrix)