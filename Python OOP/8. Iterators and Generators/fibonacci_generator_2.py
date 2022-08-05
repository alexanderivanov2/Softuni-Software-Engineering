def fibonacci():
    a = 0
    b = 1
    c = 0
    while True:
        if a > 0:
            c = a + b
        yield c

        a = b
        b = c


generator = fibonacci()
for i in range(5):
    print(next(generator))
