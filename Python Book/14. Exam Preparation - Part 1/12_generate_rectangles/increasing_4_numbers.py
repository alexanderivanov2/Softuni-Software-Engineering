n = int(input())
m = int(input())
count = True
for left in range(-n, n):
    for top in range(-n, n):
        for right in range(left + 1, n + 1):
            for bottom in range(top + 1, n + 1):
                area = abs(left - right) * abs(top - bottom)
                if area >= m:
                    print("(%d, %d) (%d, %d) -> %d" % (left, top, right, bottom, area))
                    count = False
if count:
    print(f"No")