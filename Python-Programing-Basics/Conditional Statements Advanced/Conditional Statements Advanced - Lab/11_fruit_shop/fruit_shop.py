fruit = input()
day_of_week = input()
quantity = float(input())
fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
working_days_price = [2.5, 1.2, 0.85, 1.45, 2.7, 5.5, 3.85]
rest_days_price = [2.7, 1.25, 0.9, 1.6, 3.0, 5.6, 4.2]

if day_of_week in days_of_week[:5] and fruit in fruits:
    index = fruits.index(fruit)
    price = working_days_price[index] * quantity
    print(f"{price:.2f}")
elif day_of_week in days_of_week[5:] and fruit in fruits:
    index = fruits.index(fruit)
    price = rest_days_price[index] * quantity
    print(f"{price:.2f}")
else:
    print("error")
