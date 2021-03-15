hour = int(input())
minutes = int(input()) + 15

if minutes >= 60:
    hour += 1
    minutes -= 60

if hour == 24:
    hour = 0

if minutes > 9:
    print(f"{hour}:{minutes}")
else:
    print(f"{hour}:0{minutes}")
