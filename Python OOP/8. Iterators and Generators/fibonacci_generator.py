def fibonacci():
    num_1 = 0
    num_2 = 1
    num_3 = num_1 + num_2
    while True:
        yield num_1
        num_1 = num_2
        num_2 = num_3
        num_3 = num_1 + num_2


generator = fibonacci()
for i in range(5):
    print(next(generator))