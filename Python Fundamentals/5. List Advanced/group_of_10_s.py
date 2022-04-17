nums = [int(num) for num in input().split(", ")]
current_boundary = 10
prevision_boundary = 0

while nums:
    group = [n for n in nums if prevision_boundary < n <= current_boundary]
    current_nums = nums
    nums = [n for n in current_nums if n not in group]
    print(f"Group of {current_boundary}'s: {group}")
    prevision_boundary = current_boundary
    current_boundary += 10
