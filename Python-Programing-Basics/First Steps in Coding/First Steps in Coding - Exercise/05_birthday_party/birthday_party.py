price_rent = int(input())


def calculate_budget(rent):
    budget = rent
    cake = rent * 0.20
    drinks = cake - (cake * 0.45)
    animator = rent / 3
    budget += cake + drinks + animator
    print(budget)


calculate_budget(price_rent)
