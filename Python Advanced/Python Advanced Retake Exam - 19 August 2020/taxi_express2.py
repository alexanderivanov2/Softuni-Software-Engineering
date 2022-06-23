from collections import deque

customers = deque([int(el) for el in input().split(", ")])
taxis = [int(el) for el in input().split(", ")]
total_time = 0


while taxis and customers:
    customer = customers.popleft()
    taxi = taxis.pop()
    if customer <= taxi:
        total_time += customer
    else:
        customers.appendleft(customer)

if customers:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(el) for el in customers)}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")