from collections import deque

stations = deque()

n = int(input())

for i in range(n):
    a, b = input().split()
    station_value = int(a) - int(b)
    stations.append(station_value)

index = 0

while True:
    a = stations.popleft()
    if a < 0:
        stations.append(a)
        index += 1
        continue
    station_v = a
    for station in stations:
        station_v += station
        if station_v < 0:
            break
    if station_v > 0:
        break
    stations.append(a)
    index += 1

print(index)
