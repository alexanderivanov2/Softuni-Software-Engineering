hours = int(input())
minutes = int(input())
add_minutes = minutes + 15
if add_minutes <= 59:
    hours += 0
    minutes = add_minutes
elif add_minutes >= 60:
    hours += 1
    minutes = add_minutes - 60

if hours >= 24:
    hours = 0
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")