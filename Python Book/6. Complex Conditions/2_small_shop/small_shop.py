product = input().lower()
city = input().title()
quantity = float(input())

if product == "coffee":
    if city == "Sofia":
        print(quantity * 0.50)
    elif city == "Plovdiv":
        print(quantity * 0.40)
    else:
        print(quantity * .45)
elif product == "water":
    if city == "Sofia":
        print(quantity * 0.80)
    elif city == "Plovdiv":
        print((quantity * 0.70))
    else:
        print(quantity * 0.70)
elif product == "beer":
    if city == "Sofia":
        print(quantity * 1.20)
    elif city == "Plovdiv":
        print(quantity * 1.15)
    else:
        print(quantity * 1.10)
elif product == "sweets":
    if city == "Sofia":
        print(quantity * 1.45)
    elif city == "Plovdiv":
        print(quantity * 1.30)
    else:
        print(quantity * 1.35)
else:
    if city == "Sofia":
        print(quantity * 1.60)
    elif city == "Plovdiv":
        print(quantity * 1.50)
    else:
        print(quantity * 1.55)