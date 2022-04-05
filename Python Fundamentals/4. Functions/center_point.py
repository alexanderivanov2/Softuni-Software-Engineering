from math import floor

def close_to_center(x1, x2, y1, y2):
    first_line = abs(x1) + abs(y1)
    second_line = abs(x2) + abs(y2)
    if first_line <= second_line:
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(close_to_center(x1, x2, y1, y2))
