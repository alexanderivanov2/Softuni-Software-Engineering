import math

year = input()
holidays = int(input())
weekends_in_hometown = int(input())

weekends_plays = (48 - weekends_in_hometown) * 3 / 4 + weekends_in_hometown + (holidays * 2 / 3)

if year == "leap":
    weekends_plays += weekends_plays * 0.15

print(math.floor(weekends_plays))
