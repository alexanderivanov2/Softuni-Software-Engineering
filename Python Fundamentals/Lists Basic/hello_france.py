CLOTHES = 50
SHOES = 35
ACCESSORIES = 20.50
items = input().split("|")
budget = float(input())
prices = []
win_prices = []
profit = 0

for item in items:
    type_item, price = item.split("->")
    price = float(price)
    if type_item == "Clothes" and price <= CLOTHES and budget >= price:
        budget -= price
        profit_price = price * 0.40 + price
        prices.append(profit_price)
        profit += profit_price - price
    elif type_item == "Shoes" and price <= SHOES and budget >= price:
        budget -= price
        profit_price = price * 0.40 + price
        prices.append(profit_price)
        profit += profit_price - price
    elif type_item == "Accessories" and price <= ACCESSORIES and budget >= price:
        budget -= price
        profit_price = price * 0.40 + price
        prices.append(profit_price)
        profit += profit_price - price

print(' '.join(f"{el:.2f}" for el in prices))
print(f"Profit: {profit:.2f}")
if sum(prices) + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")