from collections import deque


def create_matrix():
    n, m = [int(x) for x in input().split()]
    snake = deque([x for x in input()])
    for r in range(n):
        line = ""
        for c in range(m):
            a = snake.popleft()
            line += a
            snake.append(a)
        if r % 2 == 0:
            print(line)
        else:
            print("".join(list(reversed(line))))



create_matrix()
