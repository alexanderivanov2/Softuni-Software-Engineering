n = int(input())
down_line, stars = "-", "*"
width = 5 * n
width_down_line_left = n * 3
width_down_line_right = width - width_down_line_left - 2  # - row
height_top_to_middle = n
mid_and_end = n // 2
end_of_axe = height_top_to_middle + 1 + ((height_top_to_middle - 1) // 2)
end_down_line = (width_down_line_left - ((end_of_axe - height_top_to_middle - 1) // 2))
after_mid_downline = (height_top_to_middle - 1)
end_right_downline = (width - width_down_line_left - after_mid_downline)
print(down_line * width_down_line_left + stars * 2 + down_line * width_down_line_right)
for row in range(1, height_top_to_middle):
    print(down_line * width_down_line_left + stars + down_line * row + stars + down_line * (width_down_line_right - row))

for row2 in range(1, mid_and_end + 1):
    print(stars * (width_down_line_left + 1) + down_line * (height_top_to_middle - 1) + stars + down_line *
          (width_down_line_right - height_top_to_middle + 1))

for row3 in range(1, mid_and_end):
    if n > 2:
        print(down_line * width_down_line_left + stars + down_line * after_mid_downline + stars +
        down_line * (end_right_downline - 2))
        width_down_line_left -= 1
        after_mid_downline += 2
        end_right_downline -= 1

stars_sum = after_mid_downline + 2
right_lines = end_right_downline - 2
left_lines = width - stars_sum - right_lines
print(down_line * left_lines + stars * stars_sum + down_line * right_lines)
