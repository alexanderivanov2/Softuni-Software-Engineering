projection = input().lower()
r = int(input())
c = int(input())
incomes = 0

if projection == "premiere":
    incomes = (r*c) * 12.00
elif projection == "normal":
    incomes = (r*c) * 7.50
else:
    incomes = (r*c) * 5.00

print(f"{incomes:.2f} leva")