def get_time(racer):
    time = 0
    for race_time in racer:
        if race_time > 0:
            time += race_time
        else:
            time *= 0.8
    return time


race = [int(el) for el in input().split()]
middle = len(race) // 2
left_racer = race[:middle]
right_racer = race[-1: middle: -1]

time_left_racer = get_time(left_racer)
time_right_racer = get_time(right_racer)

if time_left_racer < time_right_racer:
    print(f"The winner is left with total time: {time_left_racer:.1f}")
else:
    print(f"The winner is right with total time: {time_right_racer:.1f}")
