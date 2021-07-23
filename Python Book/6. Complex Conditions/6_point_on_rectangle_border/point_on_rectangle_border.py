x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

left_side = (x1 == x) and (y >= y1) and (y <= y2)
right_side = (x2 == x) and (y >= y1) and (y <= y2)
up_side = (y1 == y) and (x >= x1) and (x <= x2)
down_side = (y2 == y) and (x >= x1) and (x <= x2)

if left_side or up_side or right_side or down_side:
    print("Border")
else:
    print("Inside / Outside")