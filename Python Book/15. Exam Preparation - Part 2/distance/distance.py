start_speed = int(input())
first_time = int(input()) / 100 / 0.6
second_time = int(input()) / 100 / 0.6
third_time = int(input()) / 100 / 0.6

startspeed2 = start_speed + (start_speed / 100 * 10)
start_speed3 = startspeed2 - (startspeed2 / 100 * 5)
distance = start_speed * first_time + startspeed2 * second_time + start_speed3 * third_time
print(f"{distance:.2f}")