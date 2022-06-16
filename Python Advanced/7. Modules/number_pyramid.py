def number_pyramid(n):
    for row in range(1, n + 2):
        print(*[col for col in range(1, row)])
    for row in range(n, 0, -1):
        print(*[col for col in range(1, row)])


number_pyramid(5)