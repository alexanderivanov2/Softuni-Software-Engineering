from collections import deque

josephus = deque([el for el in input().split()])
count = int(input())
new_result = []
counter = 0
while josephus:
    counter += 1
    player = josephus.popleft()
    if count == counter or len(josephus) == 0:
        counter = 0
        new_result.append(player)
        continue

    josephus.append(player)

print(f'[{",".join(new_result)}]')
