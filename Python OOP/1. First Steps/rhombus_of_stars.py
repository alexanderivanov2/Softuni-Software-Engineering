def print_rhombus(n):
    for i in range(1, n + 1):
        space = (n - i) * " "
        stars = " ".join("*" * i)
        print(space + stars)
    for i in range(1, n):
        space = " " * i
        stars = " ".join("*" * (n - i))
        print(space + stars)


print_rhombus(int(input()))
