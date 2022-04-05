def do_exchange(nums, index):
    first_part = nums[index + 1:]
    second_part = nums[:index + 1]
    nums = first_part + second_part
    return nums


def do_max(nums, type_sort):
    result = -1
    index = 0
    if type_sort == "even":
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] >= result:
                result = nums[i]
                index = i
    else:
        for i in range(len(nums)):
            if nums[i] % 2 != 0 and nums[i] >= result:
                result = nums[i]
                index = i
    if result == -1:
        return "No matches"
    return index


def do_min(nums, type_sort):
    result = 1001
    index = 0
    if type_sort == "even":
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= result:
                result = nums[i]
                index = i
    else:
        for i in range(len(nums)):
            if nums[i] % 2 != 0 and nums[i] <= result:
                result = nums[i]
                index = i
    if result == 1001:
        return "No matches"
    return index


def do_first_nums(nums, count, type_sort):
    first = []
    if len(nums) < count:
        return "Invalid count"  # check if error
    if type_sort == "even":
        for num in nums:
            if num % 2 == 0:
                first.append(num)
            if len(first) == count:
                break
    else:
        for num in nums:
            if num % 2 != 0:
                first.append(num)
            if len(first) == count:
                break
    return first


def do_last_nums(nums, count, type_sort):
    last = []
    if len(nums) < count:
        return "Invalid count"  # check if error
    if type_sort == "even":
        for num in nums[::-1]:
            if num % 2 == 0:
                last.append(num)
            if len(last) == count:
                break
    else:
        for num in nums[::-1]:
            if not num % 2 == 0:
                last.append(num)
            if len(last) == count:
                break
    return last[::-1]


nums = [int(el) for el in input().split()]

command = input()

while not command == "end":
    action, *data = command.split()
    if action == "exchange":
        index = int(data[0])
        if not (0 <= index < len(nums)):
            print("Invalid index")
        else:
            nums = do_exchange(nums, index)
    elif action == "max":
        print(do_max(nums, data[0]))
    elif action == "min":
        print(do_min(nums, data[0]))
    elif action == "first":
        count = int(data[0])
        type_sort = data[1]
        print(do_first_nums(nums, count, type_sort))
    elif action == "last":
        count = int(data[0])
        type_sort = data[1]
        print(do_last_nums(nums, count, type_sort))
    command = input()

print(nums)
