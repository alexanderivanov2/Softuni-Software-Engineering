import math

figure = input().lower()
Square = "square"
Rectangle = "rectangle"
Circle = "circle"
Triangle = "triangle"

if figure == Square:
    a = float(input())
    print(round(a*a, 3))
elif figure ==  Rectangle:
    a = float(input())
    b = float(input())
    print(round(a*b, 3))
elif figure == Circle:
    r = float(input())
    pi = math.pi
    print(round(pi * r * r, 3))
elif figure == Triangle:
    a = float(input())
    h = float(input())
    print(round((a*h)/2, 3))





