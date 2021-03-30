def get_index(day):
    if day < 10:
        return 0
    elif day <= 15:
        return 1
    elif day > 15:
        return 2


days = int(input()) - 1
room_type = input()
review = input()
apartment = [0.30, 0.35, 0.50]
president_apartment = [0.1, 0.15, 0.2]
index = get_index(days)

if room_type == "apartment":
    price = 25 * days
    price -= price * apartment[index]
elif room_type == "president apartment":
    price = 35 * days
    price -= price * president_apartment[index]
else:
    price = 18 * days

if review == "positive":
    price += price * 0.25
else:
    price -= price * 0.1

print(f"{price:.2f}")
