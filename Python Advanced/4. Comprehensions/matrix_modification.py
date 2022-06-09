def create_matrix():
    n = int(input())
    demo = [[int(j) for j in input().split()] for x in range(n)]
    return demo, n


matrix, size = create_matrix()
command = input()

while command != "END":
    do, *data = command.split()
    r, c, value = [int(x) for x in data]
    if 0 <= r < size and 0 <= c < size:
        if do == "Add":
            matrix[r][c] += value
        elif do == "Subtract":
            matrix[r][c] -= value
    else:
        print("Invalid coordinates")
    command = input()

[print(" ".join(str(el) for el in x)) for x in matrix]
