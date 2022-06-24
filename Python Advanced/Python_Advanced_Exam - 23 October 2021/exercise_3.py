def shopping_list(money, **kwargs):
    budget = money
    if budget < 100:
        return "You do not have enough budget."
    boughts = []
    dicts = kwargs
    for key, value in dicts.items():
        price = value[0] * value[1]
        if price <= budget:
            budget -= price
            boughts.append(f"You bought {key} for {price:.2f} leva.")
        if len(boughts) == 5:
            break
    return '\n'.join(boughts)



print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))