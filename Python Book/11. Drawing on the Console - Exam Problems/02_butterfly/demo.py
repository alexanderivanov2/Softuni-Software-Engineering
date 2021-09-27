n = int(input())
n_is_even = n % 2 == 0
width = 2 * n - 1
height = 2 * (n - 2) + 1
left_or_right_part_width = n - 1
left, right, star, dash, center, space = "\\", "/", "*", "-", "@", " "

for up_half in range(1, (height - 1) // 2 + 1):
    if not up_half % 2 == 0:
        print(star * (left_or_right_part_width - 1) + left + space + right + star * (left_or_right_part_width - 1))
    else:
        print(dash * (left_or_right_part_width - 1) + left + space + right + dash * (left_or_right_part_width - 1))

print(space * left_or_right_part_width + center + space * left_or_right_part_width)
