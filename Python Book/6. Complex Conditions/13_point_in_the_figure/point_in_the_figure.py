h = int(input())
x = int(input())
y = int(input())

x1 = 0
x2 = 3 * h
x3 = h * 2 - h
x4 = h * 2
y1 = 0
y2 = h
y3 = h
y4 = h * 4

inside_border = (y == y2 and x3 < x < x4)
inside = x1 < x < x2 and y1 < y < y2 or (y == y2 and x1 <= x <= x2) or (x3 < x < x4 and y3 < y < y4)\
         or (y == y3 and x3 <= x <= x4)
border = (x == x1 and y1 <= y <= y2) or (x == x2 and y1 <= y <= y2) or (y == y1 and x1 <= x <= x2) or \
         (y == y2 and x1 <= x <= x2) or (x == x3 and y3 <= y <= y4) or (x == x4 and y3 <= y <= y4) or \
         (y == y3 and x3 <= x <= x4) or (y == y4 and x3 <= x <= x4)

if inside or border:
    if inside_border:
        print("inside")
    elif border:
        print("border")
    else:
        print("inside")
else:
        print("outside")