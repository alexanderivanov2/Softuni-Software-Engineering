from collections import deque

pizza_orders = deque([int(order) for order in input().split(", ") if 0 < int(order) < 11])
employees = [int(employ) for employ in input().split(", ")]
total_pizza = 0

while len(pizza_orders) > 0 and len(employees) >0:
    order = pizza_orders.popleft()
    employ = employees.pop()
    if employ >= order:
        total_pizza += order
        continue
    else:
        order -= employ
        total_pizza += employ
        pizza_orders.appendleft(order)


if len(pizza_orders) == 0:
    print(f"All orders are successfully completed!\nTotal pizzas made: {total_pizza}\nEmployees: {', '.join([str(el) for el in employees])}")
else:
    print(f"Not all orders are completed.\nOrders left: {', '.join([str(el) for el in pizza_orders])}")