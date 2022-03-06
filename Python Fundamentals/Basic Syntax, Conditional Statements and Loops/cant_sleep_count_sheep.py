def count_sheep(n):
    for i in range(1, n + 1):
        print(f"{i} sheep...", end="")


sheep = int(input())
count_sheep(sheep)
