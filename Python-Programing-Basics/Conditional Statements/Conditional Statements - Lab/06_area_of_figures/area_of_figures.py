from math import pi


def calculate_area_of_square():
    a = float(input())
    return a * a


def calculate_area_of_rectangle():
    a = float(input())
    b = float(input())
    return a * b


def calculate_area_of_circle():
    radius = float(input())
    p = pi
    return p * radius ** 2


def calculate_area_of_triangle():
    side = float(input())
    height = float(input())
    return (side * height) / 2


figure = input()
area = 0

if "square" == figure:
    area = calculate_area_of_square()
elif "rectangle" == figure:
    area = calculate_area_of_rectangle()
elif "circle" == figure:
    area = calculate_area_of_circle()
elif "triangle" == figure:
    area = calculate_area_of_triangle()

print(f"{area:.3f}")
