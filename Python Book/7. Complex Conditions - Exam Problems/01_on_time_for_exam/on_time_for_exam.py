hour_exam = int(input())
min_exam = int(input())
hour_arrive = int(input())
min_arrive = int(input())


minutes_exam = hour_exam * 60 + min_exam
minutes_arrive = hour_arrive * 60 + min_arrive

if hour_exam == 0:
    minutes_exam = 24 * 60 + min_exam
elif hour_arrive == 0:
    minutes_arrive = 24 * 60 + min_arrive

late = minutes_arrive - minutes_exam
early = minutes_exam - minutes_arrive
hours = 0
mins = 0

if minutes_arrive > minutes_exam:
    if late <= 59:
        mins = late
    else:
        hours = late // 60
        mins = late % 60
elif minutes_exam > minutes_arrive:
    if early <= 59:
        mins = early
    else:
        hours = early // 60
        mins = early % 60
else:
    print("On Time")

if minutes_arrive > minutes_exam:
    if hours > 0:
        if mins < 10:
            print(f"Late\n{hours}:0{mins} hours after the start")
        else:
            print(f"Late\n{hours}:{mins} hours after the start")
    elif hours == 0:
        if mins < 10:
            print(f"Late\n{mins} minutes after the start")
        else:
            print(f"Late\n{mins} minutes after the start")
elif minutes_exam > minutes_arrive:
    if early <= 30:
        print(f"On time\n{mins} minutes before the start")
    elif hours > 0:
        if mins < 10:
            print(f"Early\n{hours}:0{mins} hours before the start")
        else:
            print(f"Early\n{hours}:{mins} hours before the start")
    else:
        if mins < 10:
            print(f"Early\n{mins} minutes before the start")
        else:
            print(f"Early\n{mins} minutes before the start")