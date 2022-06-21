from collections import deque

males = [int(el) for el in input().split()]
females = deque(int(el) for el in input().split())
matches = 0

while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.pop()
        continue
    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue
    elif females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if males[-1] == females[0]:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(el) for el in reversed(males)])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")
