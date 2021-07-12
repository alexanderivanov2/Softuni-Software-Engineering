rest_days = int(input())
year_in_days = 365
work_days = year_in_days - rest_days
play_time = (work_days * 63 + rest_days * 127)

if play_time <= 30000:
    play_time1 = 30000 - play_time
else:
    play_time1 = play_time - 30000

hours = play_time1 // 60
minutes = play_time1 % 60

if play_time > 30000:
    print(f"Tom will run away\n{hours} hours and {minutes} minutes more for play")
else:
    print(f"Tom sleeps well\n{hours} hours and {minutes} minutes less for play")
