while True:
    try:
        n = int(input())
        if n % 2 == 0:
            print(n)
            break
        else:
            print("Need even number: ")
    except ValueError:
        print("Invalid number.")