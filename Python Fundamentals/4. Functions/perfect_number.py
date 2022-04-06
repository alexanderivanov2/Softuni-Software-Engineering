def check_is_perfect_number(num):
    half = num // 2
    nums = [el for el in range(half, 0, -1) if num % el == 0]
    if num == sum(nums):
        return "We have a perfect number!"
    return "It's not so perfect."


num = int(input())
print(check_is_perfect_number(num))
