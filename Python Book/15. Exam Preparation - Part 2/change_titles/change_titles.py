import math

money = float(input())
width_floor = float(input())
height_floor = float(input())
a_triangle = float(input())
h_triangle = float(input())
price_plate = float(input())
builder_price = float(input())

area_rectangle = width_floor * height_floor
are_plates = (a_triangle * h_triangle) / 2
need_plates = math.ceil((area_rectangle / are_plates) + 5 )
need_money = (need_plates * price_plate) + builder_price

if money >= need_money:
    print(f"{abs(money - need_money):.2f} lv left.")
else:
    print(f"You'll need {abs(need_money - money):.2f} lv more.")