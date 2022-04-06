def calculate_price(stock, quantity):
    return f"{quantity * prices[stock]:.2f}"


prices = {"coffee": 1.50,
          "water": 1.00,
          "coke": 1.40,
          "snacks": 2.00
          }

order_stock = input()
quantity = int(input())
print(calculate_price(order_stock, quantity))
