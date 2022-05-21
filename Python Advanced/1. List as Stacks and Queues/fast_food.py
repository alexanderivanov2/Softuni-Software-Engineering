from collections import deque

quantity_of_food = int(input())
orders = deque([(int(x)) for x in input().split()])
print(max(orders))
range_num = len(orders)
left_orders = []
for _ in range(range_num):
    quantity = orders.popleft()
    if quantity <= quantity_of_food:
        quantity_of_food -= quantity
    else:
        left_orders.append(str(quantity))
        break

while orders:
    left_orders.append(str(orders.popleft()))

if left_orders:
    print(f"Orders left: {' '.join(left_orders)}")
else:
    print("Orders complete")
