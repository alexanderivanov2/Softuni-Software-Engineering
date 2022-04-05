nums = [int(el) for el in input().split()]
sort_nums = sorted(nums)
n = int(input())

for el in sort_nums[:n]:
    nums.remove(el)

print(', '.join(str(el) for el in nums))