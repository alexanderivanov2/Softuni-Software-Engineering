from math import floor
year = input().lower()
holidays = int(input())
weekends_go_home = int(input())
weekends_sofia = 48 - weekends_go_home
weekends_not_work = 3 / 4 * weekends_sofia / 1
weekends_plays = (weekends_not_work + weekends_go_home)
plays_in_holidays = 2 / 3 * holidays/1
plays = 0

if year == "leap":
    plays = plays_in_holidays + weekends_plays
    plays *= 1.15
else:
    plays = plays_in_holidays + weekends_plays

print(f"{floor(plays)}")