from math import floor


def order_cor(cordinates_line):
    line_a = abs(cordinates_line[0]) + abs(cordinates_line[1])
    line_b = abs(cordinates_line[2]) + abs(cordinates_line[3])
    if line_a <= line_b:
        return f"({floor(cordinates_line[0])}, {floor(cordinates_line[1])})({floor(cordinates_line[2])}, {floor(cordinates_line[3])})"
    else:
        return f"({floor(cordinates_line[2])}, {floor(cordinates_line[3])})({floor(cordinates_line[0])}, {floor(cordinates_line[1])})"


def calculate_range(cordinates_line):
    a = abs(cordinates_line[0] + cordinates_line[1])
    b = abs(cordinates_line[2] + cordinates_line[3])
    cordinates_line = order_cor(cordinates_line)
    return a + b, cordinates_line


def check_longer_line(cordinates):
    line_one, line_one_cordinates = calculate_range(cordinates[:len(cordinates) // 2])
    line_two, line_two_cordinates = calculate_range(cordinates[len(cordinates) // 2 :])
    if line_one >= line_two:
        return line_one_cordinates
    else:
        return line_two_cordinates


cordinates = []

for i in range(8):
    cordinates.append(float(input()))

print(check_longer_line(cordinates))
