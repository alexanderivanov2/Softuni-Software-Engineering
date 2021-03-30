projection = (input())
r = int(input())
c = int(input())

if projection == "Premiere":
    profit = r * c * 12
elif projection == "Normal":
    profit = r * c * 7.50
else:
    profit = r * c * 5

print(f"{profit:.2f} leva")
