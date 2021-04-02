exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

if exam_hour > arrive_hour or exam_hour == arrive_hour and exam_min >= arrive_min:
    if exam_hour == arrive_hour or (exam_hour - 1 == arrive_hour and 0 != (exam_min + arrive_min) < 60):
        if exam_min == 0:
            min_before = 60 - arrive_min
        else:
            min_before = abs(exam_min - arrive_min)
        if min_before <= 30 or min_before == 60:
            print("On time")
        else:
            print("Early")
        if min_before != 60:
            print(f"{min_before} minutes before the start")
    else:
        if exam_min > arrive_min:
            min_before = exam_min - arrive_min
            hour_before = exam_hour - arrive_hour
        elif arrive_min > exam_min:
            min_before = exam_min + (60 - arrive_min)
            hour_before = exam_hour - arrive_hour - 1
        else:
            hour_before = exam_hour - arrive_hour
            min_before = 0

        if hour_before == 0 and min_before <= 30:
            print("On time")
        else:
            print("Early")

        if hour_before == 0:
            print(f"{min_before} minutes before the start")
        elif min_before > 9:
            print(f"{hour_before}:{min_before} hours before the start")
        else:
            print(f"{hour_before}:0{min_before} hours before the start")
else:
    if exam_hour == arrive_hour or (arrive_hour - 1 == exam_hour and 0 != exam_min + arrive_min < 60 and exam_min > arrive_min):
        if arrive_min < exam_min:
            min_after = (60 - exam_min) + arrive_min
        else:
            min_after = arrive_min - exam_min
        print("Late")
        print(f"{min_after} minutes after the start")
    else:
        if exam_min > arrive_min:
            min_after = arrive_min + (60 - exam_min)
            hour_after = arrive_hour - exam_hour - 1
        elif arrive_min > exam_min:
            min_after = arrive_min - exam_min
            hour_after = arrive_hour - exam_hour
        else:
            hour_after = arrive_hour - exam_hour
            min_after = 0

        print("Late")

        if min_after > 9:
            print(f"{hour_after}:{min_after} hours after the start")
        else:
            print(f"{hour_after}:0{min_after} hours after the start")
