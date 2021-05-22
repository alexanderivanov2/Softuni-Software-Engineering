import math

number_paint_boxes = int(input())
number_carpets = int(input())
pair_gloves_price = float(input())
brush_price = float(input())

gloves_number = math.ceil(number_carpets * 0.35)
brush_number = math.floor(number_paint_boxes * 0.48)

total_price = number_paint_boxes * 21.50 + number_carpets * 5.20 + gloves_number * pair_gloves_price\
              + brush_number * brush_price
delivery_cost = total_price / 15

print(f"This delivery will cost {delivery_cost:.2f} lv.")