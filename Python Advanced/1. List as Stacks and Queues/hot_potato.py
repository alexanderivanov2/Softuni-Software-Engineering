from collections import deque

names = input().split()
players = deque()

for name in names:
    players.append(name)

num = int(input())

count = 0

while not len(players) == 1:
    count += 1
    if count == num:
        print(f"Removed {players.popleft()}")
        count = 0
    else:
        a = players.popleft()
        players.append(a)

print(f"Last is {players.popleft()}")