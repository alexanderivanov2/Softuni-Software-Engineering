clothes_in_box = [int(x) for x in input().split()]
capacity_of_rack = int(input())
sum_of_clothes = 0
racks = 1

while clothes_in_box:
    a = clothes_in_box.pop()
    if a + sum_of_clothes <= capacity_of_rack:
        sum_of_clothes += a
    else:
        clothes_in_box.append(a)
        racks += 1
        sum_of_clothes = 0

print(racks)