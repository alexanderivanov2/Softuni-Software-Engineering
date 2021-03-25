hour = int(input())
day = input()

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
working_hours = range(10, 19)

if day in working_days and hour in working_hours:
    print("open")
else:
    print("closed")
