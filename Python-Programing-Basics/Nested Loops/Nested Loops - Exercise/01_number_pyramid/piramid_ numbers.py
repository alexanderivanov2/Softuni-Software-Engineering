num = int(input())
number = 0
for row in range(1, num + 1):
    for n in range(1, row + 1):
        number += 1
        print(f"{number}", end=" ")
        if number == num:
            exit()
    print()