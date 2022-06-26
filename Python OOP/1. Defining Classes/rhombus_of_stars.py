def build_top(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for i2 in range(i):
            print("*", end=" ")
        print()


def build_bottom(n):
    for i in range(1, n):
        print(" " * i, end='')
        for i2 in range(n - i, 0, -1):
            print("*", end=' ')
        print()


def create_rhombus():
    n = int(input())
    build_top(n)
    build_bottom(n)


create_rhombus()
