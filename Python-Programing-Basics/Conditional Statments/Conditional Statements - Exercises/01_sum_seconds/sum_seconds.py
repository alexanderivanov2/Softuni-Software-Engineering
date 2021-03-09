competitor_one = int(input())
competitor_two = int(input())
competitor_three = int(input())

all_time = competitor_one + competitor_two + competitor_three
minutes = all_time // 60
seconds = all_time % 60

if seconds > 9:
    print(f"{minutes}:{seconds}")
else:
    print(f"{minutes}:0{seconds}")
