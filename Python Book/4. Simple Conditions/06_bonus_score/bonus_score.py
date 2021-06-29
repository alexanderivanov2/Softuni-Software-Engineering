number = int(input())
bonus = 0

if number <= 99:
    bonus = 5
elif 100 <= number <= 999:
    bonus = number * (20 / 100)
elif number > 1000:
    bonus = number * (10 / 100)

if number % 2 == 0:
    bonus = bonus + 1
elif number % 10 == 5:
    bonus = bonus + 2

number1 = number + bonus

print(bonus)
print(number1)
