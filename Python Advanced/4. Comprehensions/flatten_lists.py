matrix_split = [str(x) for x in input().split("|")]
matrix = [matrix_split[i].split() for i in range(len(matrix_split) - 1, -1, -1)]
flat = [num for row in matrix for num in row]
print(" ".join(str(x) for x in flat))
