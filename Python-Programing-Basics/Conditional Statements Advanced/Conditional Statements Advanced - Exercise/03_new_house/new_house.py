def get_index(flower_n):
    if flower_n == "Roses":
        return 0
    elif flower_n == "Dahlias":
        return 1
    elif flower_n == "Tulips":
        return 2
    elif flower_n == "Narcissus":
        return 3
    elif flower_n == "Gladiolus":
        return 4


flower = input()
count_of_flowers = int(input())
budget = int(input())
flowers = ["Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"]
index = get_index(flower)
prices = [5, 3.80, 2.80, 3, 2.50]
price = 0

if flower == "Roses":
    price = prices[index] * count_of_flowers
    if count_of_flowers > 80:
        price *= 0.90
elif flower == "Dahlias":
    price = prices[index] * count_of_flowers
    if count_of_flowers > 90:
        price *= 0.85
elif flower == "Tulips":
    price = prices[index] * count_of_flowers
    if count_of_flowers > 80:
        price *= 0.85
elif flower == "Narcissus":
    price = prices[index] * count_of_flowers
    if count_of_flowers < 120:
        price *= 1.15
elif flower == "Gladiolus":
    price = prices[index] * count_of_flowers
    if count_of_flowers < 80:
        price *= 1.20

if budget >= price:
    print(f"Hey, you have a great garden with {count_of_flowers} {flower} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
