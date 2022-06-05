rows, columns = input().split(", ")
total_sum = 0
matrix = []

for row in range(int(rows)):
    matrix.append([])
    elements = input().split(", ")
    for element in elements:
        matrix[row].append(int(element))
    total_sum += sum(matrix[row])

print(total_sum)
print(matrix)
