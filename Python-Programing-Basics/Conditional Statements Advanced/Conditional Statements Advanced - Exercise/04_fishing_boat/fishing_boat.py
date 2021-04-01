def get_discount(fisherman):
    if fisherman < 7:
        return 0.90
    elif fisherman < 12:
        return 0.85
    else:
        return 0.75


budget = int(input())
season = input()
fishermans = int(input())
discount = get_discount(fishermans)
price = 0

if season == "Spring":
    price = 3000 * discount
elif season in ["Summer", "Autumn"]:
    price = 4200 * discount
elif season == "Winter":
    price = 2600 * discount

if season != "Autumn" and fishermans % 2 == 0:
    price *= 0.95

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
