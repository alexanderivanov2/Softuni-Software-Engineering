n = int(input())
n_is_even = n % 2 == 0
right_line = "/"
left_line = chr(92)
down_line = "_"
up_middle = "^"
side = "|"
space = " "
between_left_right = n - (n // 2 + 2)

print(right_line + up_middle * (n // 2) + left_line + down_line * (between_left_right * 2) + right_line + up_middle
      * (n // 2) + left_line)

for row in range(1, n - 1):
    if row == n - 1 - 1:
        print(side + space * (n // 2 + 1) + down_line * (between_left_right * 2) + space * (n // 2 + 1) + side)
    else:
        print(side + space * (n * 2 - 2) + side)

print(left_line + down_line * (n // 2) + right_line + space * (between_left_right * 2) + left_line + down_line *
      (n // 2) + right_line)