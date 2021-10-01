n = int(input())

points, downline, left_line, right_line, text = ".", "_", "\\", "//", "STOP!"
top_points = n + 1
down_points = n - 1
top_downline = n * 2 + 1
middle_downline_up_to_down = top_downline - 2 # + 2 to middle, - 2 after middle
left_right_side_middle = (middle_downline_up_to_down - 7 + (top_points * 2)) // 2
downline_after_middle = (middle_downline_up_to_down - 2 + (top_points * 2))
down_after_mid = 2