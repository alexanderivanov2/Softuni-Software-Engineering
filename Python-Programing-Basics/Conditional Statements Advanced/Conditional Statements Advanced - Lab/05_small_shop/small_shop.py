product = input()
city = input()
quality = float(input())

coffee = [0.50, 0.40, 0.45]
water = [0.80, 0.70, 0.70]
beer = [1.20, 1.15, 1.10]
sweets = [1.45, 1.30, 1.35]
peanuts = [1.60, 1.50, 1.55]
result = 0

if city == "Sofia":
    if product == "coffee":
        result = coffee[0] * quality
    elif product == "water":
        result = water[0] * quality
    elif product == "beer":
        result = beer[0] * qualityss
    elif product == "sweets":
        result = sweets[0] * quality
    elif product == "peanuts":
        result = peanuts[0] * quality
elif city == "Plovdiv":
    if product == "coffee":
        result = coffee[1] * quality
    elif product == "water":
        result = water[1] * quality
    elif product == "beer":
        result = beer[1] * quality
    elif product == "sweets":
        result = sweets[1] * quality
    elif product == "peanuts":
        result = peanuts[1] * quality
else:
    if product == "coffee":
        result = coffee[2] * quality
    elif product == "water":
        result = water[2] * quality
    elif product == "beer":
        result = beer[2] * quality
    elif product == "sweets":
        result = sweets[2] * quality
    elif product == "peanuts":
        result = peanuts[2] * quality

print(result)
