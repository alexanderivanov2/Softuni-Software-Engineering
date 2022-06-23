from collections import deque

customers = deque(int(cust) for cust in input().split(", "))
drivers = [int(driver) for driver in input().split(", ")]
time = 0

while drivers and customers:
    if drivers[-1] < customers[0]:
        drivers.pop()
        continue
    time += customers.popleft()
    drivers.pop()

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(el) for el in customers)}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {time} minutes")