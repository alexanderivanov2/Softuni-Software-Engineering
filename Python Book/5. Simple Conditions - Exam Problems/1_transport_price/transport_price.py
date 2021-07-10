n_km = int(input())
day_night = input()
day = "day"
night = "night"

if n_km < 20 and day_night == 'day':
    price = 0.70 + (n_km * 0.79)
    print(price)
elif n_km < 20 and day_night == 'night':
    price = 0.70 + (n_km * 0.90)
    print(price)
elif n_km >= 20 and n_km < 100:
    price = n_km * 0.09
    print(price)
elif n_km >= 100:
    price = n_km * 0.06
    print(price)