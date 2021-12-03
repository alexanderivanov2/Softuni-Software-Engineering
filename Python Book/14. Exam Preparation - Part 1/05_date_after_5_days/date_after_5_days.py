d = int(input())
m = int(input())

days_in_month = 31

if m == 2:
    days_in_month = 28
elif m == 4 or m == 6 or m == 9 or m == 11:
    days_in_month = 30

if d + 5 > days_in_month:
    d = (d + 5) - days_in_month
    m += 1
    if m > 12:
        m = 1
else:
    d += 5


if m < 10:
    print(f"{d}.0{m}")
else:
    print(f"{d}.{m}")