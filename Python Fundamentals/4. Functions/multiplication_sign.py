def result(nums):
    if "zero" in nums:
        return "zero"
    elif nums.count("positive") == 3 or nums.count("positive") == 1:
        return "positive"
    else:
        return "negative"


def get_nums_result():
    nums = []
    for i in range(3):
        num = int(input())
        if num == 0:
            nums.append("zero")
        elif num < 0:
            nums.append("negative")
        else:
            nums.append("positive")
    return nums


nums = get_nums_result()
print(result(nums))
