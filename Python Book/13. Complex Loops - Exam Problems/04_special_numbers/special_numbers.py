special_number = int(input())

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if (special_number % num1 == 0 and special_number % num2 == 0 and special_number % num3 == 0 and
                        special_number % num4 == 0):
                    print(str(num1) + str(num2) + f"{num3}{num4}", end=" ")