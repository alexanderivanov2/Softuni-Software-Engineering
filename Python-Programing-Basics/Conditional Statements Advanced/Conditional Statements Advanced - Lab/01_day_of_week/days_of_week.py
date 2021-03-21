number = int(input())

days_of_week = ["Error", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if number not in range(1, 8):
    print(days_of_week[0])
else:
    print(days_of_week[number])
