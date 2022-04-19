lines = int(input())
chairs = 0
visitors = 0
game = True

for line in range(1, lines + 1):
    room = input().split()
    chairs_room = len(room[0])
    visitors_room = int(room[1])
    if visitors_room > chairs_room:
        game = False
        print(f"{int(room[1]) - len(room[0])} more chairs needed in room {line}")
        continue
    chairs += chairs_room
    visitors += visitors_room

if game:
    print(f"Game On, {chairs - visitors} free chairs left")
