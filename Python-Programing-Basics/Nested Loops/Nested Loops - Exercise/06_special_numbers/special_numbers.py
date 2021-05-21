number = int(input())

for one in range(1, 10):
    for two in range(1, 10):
        for three in range(1, 10):
            for four in range(1, 10):
                if number % one == 0 and number % two == 0 and number % three == 0 and number % four == 0:
                    print(f"{one}{two}{three}{four}", end=" ")
