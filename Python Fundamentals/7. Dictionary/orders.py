stocks = {}
command = input()

while not command == "buy":
    name, price, quantity = command.split()
    if name not in stocks:
        stocks[name] = {'price': 0, 'quantity': 0}
    stocks[name]['price'] = float(price)
    stocks[name]['quantity'] += int(quantity)
    command = input()


for key, value in stocks.items():
    result = value['price'] * value['quantity']
    print(f"{key} -> {result:.2f}")