n = int(input())

left_side = 0
right_side = 0

for i in range(n):
    num = int(input())
    left_side += num

for i in range(n):
    num = int(input())
    right_side += num

if left_side == right_side:
    print(f"Yes, sum = {left_side}")
else:
    print(f"No, diff = {abs(left_side - right_side)}")
