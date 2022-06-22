from collections import deque


def best_list_pureness(*args):
    nums = deque(args[0])
    rotate = args[1]
    pureness = [0, 0]
    count = 0
    while count <= rotate:
        score = 0
        for i in range(len(nums)):
            score += nums[i] * i
        if score > pureness[0]:
            pureness = [score, count]
        count += 1
        num = nums.pop()
        nums.appendleft(num)
    return f"Best pureness {pureness[0]} after {pureness[1]} rotations"






test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)