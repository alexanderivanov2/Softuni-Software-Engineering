import math

need_hours = int(input())
days = int(input())
workers = int(input())
days -= days * (10/100)
workhours_per_day = 10 * workers
final_result = days * workhours_per_day

if final_result >= need_hours:
    hours_left = final_result - need_hours
    print(f"Yes!{math.floor(hours_left)} hours left.")
else:
    hours_need = need_hours - final_result
    print(f"Not enough time!{math.floor(hours_need)} hours needed.")