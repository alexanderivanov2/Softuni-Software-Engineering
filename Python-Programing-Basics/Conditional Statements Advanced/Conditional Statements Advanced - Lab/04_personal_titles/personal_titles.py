years = float(input())
sex = input()

if years < 16:
    if sex == "m":
        print("Master")
    else:
        print("Miss")
else:
    if sex == "m":
        print("Mr.")
    else:
        print("Ms.")
