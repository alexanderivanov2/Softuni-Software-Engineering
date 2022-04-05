number = float(input())
while True:
    if 1 > number or number > 100:
        number = float(input())
    else:
        print(f"The number {number} is between 1 and 100")
        break
