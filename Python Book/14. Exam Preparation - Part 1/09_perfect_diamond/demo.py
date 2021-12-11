n = int(input())
star = "*"
space = " "
line = "-"
space_down = n - 1
space_up = n - (n - 1)

if n > 1:
    print(space * space_down + star)

    for row in range(1, n):
        space_down -= 1
        print(space * space_down, end="")
        print(star, end="")
        for col in range(1, row + 1):
            print(line, end="")
            print(star, end="")
        print()