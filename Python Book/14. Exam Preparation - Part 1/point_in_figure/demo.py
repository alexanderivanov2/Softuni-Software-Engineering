x = int(input())
y = int(input())

x1, y1, x2, y2, x3, y3, x4, y4 = 4, 3, 10, -5, 2, 1, 12, -3

if x1 <= x <= x2 and y1 >= y >= y2 or (x3 <= x <= x4 and y3 >= y >= y4):
    print("in")
else:
    print("out")
