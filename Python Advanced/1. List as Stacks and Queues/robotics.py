from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
time = datetime.strptime(input(), '%H:%M:%S')
robots = []
products = []
available_robots = []

for el in data:
    robot_data = el.split("-")
    robot = {}
    robot['name'] = robot_data[0]
    robot['processing_time'] = int(robot_data[1])
    robot['available'] = time
    robots.append(robot)
    available_robots.append(robot)

product = input()

while product != "End":
    products.append(product)
    product = input()

time = time + timedelta(seconds=1)
available_robots = deque(robots)
products = deque(products)

while len(products) > 0:
    product = products.popleft()

    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available'] = time + timedelta(seconds=current_robot['processing_time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['available'] = time + timedelta(seconds=current_robot['processing_time'])
        print(f"{robot['name']} - {product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r['available']:
                available_robots.append(r)
        if not available_robots:
            products.append(product)
        else:
            current_robot = available_robots.popleft()
            current_robot['available'] = time + timedelta(seconds=current_robot['processing_time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available'] = time + timedelta(seconds=current_robot['processing_time'])
            print(f"{robot['name']} - {product} [{time.strftime('%H:%M:%S')}]")
    time = time + timedelta(seconds=1)
