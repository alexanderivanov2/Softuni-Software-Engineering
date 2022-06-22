from collections import deque

jobs = deque([int(el) for el in input().split(", ")])
index = int(input())
need_job = jobs[index]
cycles = need_job
jobs[index] = 0

for el in jobs:
    if el <= need_job:
        cycles += el

print(cycles)



