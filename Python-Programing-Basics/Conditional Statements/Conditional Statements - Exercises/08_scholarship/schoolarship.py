import math

income = float(input())
success_rate = float(input())
min_work_wage = float(input())
scholarship1, scholarship2 = 0, 0

if income >= min_work_wage and success_rate >= 4.5 and success_rate >= 5.5:

    if success_rate >= 5.5:
        scholarship1 = success_rate * 25

    if income <= min_work_wage:
        scholarship2 = min_work_wage * 0.35

    if scholarship1 >= scholarship2:
        print(f"You get a scholarship for excellent results {math.floor(scholarship1)} BGN")
    else:
        print(f"You get a Social scholarship {math.floor(scholarship2)} BGN")
elif success_rate >= 5.5:
    scholarship1 = success_rate * 25
    print(f"You get a scholarship for excellent results {math.floor(scholarship1)} BGN")
elif income <= min_work_wage and success_rate >= 4.5:
    scholarship2 = min_work_wage * 0.35
    print(f"You get a Social scholarship {math.floor(scholarship2)} BGN")
else:
    print("You cannot get a scholarship!")
