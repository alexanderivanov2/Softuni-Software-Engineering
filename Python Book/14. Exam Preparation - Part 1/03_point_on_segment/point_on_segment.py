begin = int(input())
ending = int(input())
point = int(input())

left = min(begin, ending)
right = max(begin, ending)

distance_left = abs(left - point)
distance_right = abs(right - point)
min_distance = min(distance_left, distance_right)

if left <= point <= right:
    print("in")
else:
    print("out")

print(min_distance)