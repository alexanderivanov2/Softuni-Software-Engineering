tuple_numbers = tuple(map(float, input().split()))
nums = {}

for num in tuple_numbers:
    if num not in nums:
        nums[num] = tuple_numbers.count(num)

for (key, value) in nums.items():
    print(f"{key} - {value} times")