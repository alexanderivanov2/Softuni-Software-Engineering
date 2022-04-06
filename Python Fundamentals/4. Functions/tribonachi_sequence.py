def do_tribonachi_sequence(num):
    nums = [1, 1, 2]
    if num == 1:
        return nums[:1]
    elif num == 2:
        return nums[:2]
    elif num == 3:
        return nums

    while not len(nums) == num:
        c = nums[-1] + nums[-2] + nums[-3]
        nums.append(c)
    return nums


num = int(input())

result = do_tribonachi_sequence(num)
print(*result)
