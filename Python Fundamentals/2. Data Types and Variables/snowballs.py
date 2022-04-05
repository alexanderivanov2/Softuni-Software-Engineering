n = int(input())
value = 0
string = ""

for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > value:
        value = snowball_value
        string = f"{snowball_snow} : {snowball_time} = {int(snowball_value)} ({snowball_quality})"

print(string)
