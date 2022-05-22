from collections import deque
import datetime


def sort_robots_name(robots_2):
    for key in robots_2.keys():
        key1 = key
        return key1


def sort_robots_time(robots_2):
    robots_2 = dict(sorted(robots_2.items(), key=lambda x: (x[1]["free"])))
    return robots_2


robots_line = input().split(";")
hms = input().split(":")
time = datetime.timedelta(hours=int(hms[0]), minutes=int(hms[1]), seconds=int(hms[2]))
add_sec = datetime.timedelta(seconds=1)
time += add_sec
robots = {}

for robot in robots_line:
    name, w_time = robot.split("-")
    work_time = datetime.timedelta(seconds=int(w_time))
    robots[name] = {"free": time, "work_time": work_time}

products = deque()
product = input()

while not product == "End":
    products.append(product)
    product = input()

robots_one_name = sort_robots_name(robots)

while products:
    working = products.popleft()
    if time >= robots[robots_one_name]["free"]:
        robots[robots_one_name]["free"] = time + robots[robots_one_name]["work_time"]
        if time < datetime.timedelta(hours=10):
            print(f"{robots_one_name} - {working} [0{time}]")
        else:
            print(f"{robots_one_name} - {working} [{time}]")
        robots = sort_robots_time(robots)
        robots_one_name = sort_robots_name(robots)
        time += add_sec
        continue
    products.append(working)
    time += add_sec