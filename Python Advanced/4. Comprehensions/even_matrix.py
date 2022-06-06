size = int(input())
matrix = [[int(j) for j in input().split(", ") if int(j) % 2 == 0] for x in range(size)]
print(matrix)
