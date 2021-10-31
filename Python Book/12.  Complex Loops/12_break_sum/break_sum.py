has_to_end = False
for i in range(1, 4):
    if has_to_end == False:
        for j in range(3, 0, -1):
            if i + j == 2:
                has_to_end = True
                break
            print(f"{i} {j}")