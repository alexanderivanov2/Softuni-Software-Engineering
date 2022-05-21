from collections import deque

bullet_price = int(input())
barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
budget = int(input())
barrel_counter = 0
lock = None
total_bullets = 0
total_locks = len(locks)

while True:
    bullet = bullets.pop()
    lock = locks.popleft()
    barrel_counter += 1
    total_bullets += 1

    if bullet <= lock:
        print("Bang!")
        lock = None
        total_locks -= 1
    else:
        print("Ping!")
        locks.appendleft(lock)

    if barrel_counter == barrel and len(bullets) > 0:
        barrel_counter = 0
        print("Reloading!")
    if len(bullets) == 0 or len(locks) == 0:
        break

money_earned = budget - (bullet_price * total_bullets)

if len(bullets) == 0 and len(locks) > 0:
    print(f"Couldn't get through. Locks left: {total_locks}")
else:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
