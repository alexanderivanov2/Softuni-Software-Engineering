magic_number = int(input())

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                for num5 in range(1, 10):
                    for num6 in range(1, 10):
                        if num1 * num2 * num3 * num4 * num5 * num6 == magic_number:
                            print(str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6), end=" ")