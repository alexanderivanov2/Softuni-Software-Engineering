n = int(input())
n_is_even = n % 2 == 0
width = 2 * n - 1
height = 2 * (n - 2) + 1
left_or_right_part_width = n - 1
left, right, star, dash, center, space = "\\", "/", "*", "-", "@", " "