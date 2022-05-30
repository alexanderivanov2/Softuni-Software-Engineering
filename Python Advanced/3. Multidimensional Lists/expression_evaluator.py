from collections import deque
from math import floor


def subtract(nums):
    res = int(nums.popleft())
    while nums:
        res -= int(nums.popleft())
    return res


def add(nums):
    res = int(nums.popleft())
    while nums:
        res += int(nums.popleft())
    return res

def multiply(nums):
    res = int(nums.popleft())
    while nums:
        res *= int(nums.popleft())
    return res

def divide(nums):
    res = int(nums.popleft())
    while nums:
        res = floor(res / int(nums.popleft()))
    return res


sequence = deque(el for el in input().split())
nums = deque()
result = 0

while sequence:
    el = sequence.popleft()
    if el.isdigit() or len(el) > 1:
        nums.append(el)
        continue
    elif el == "-":
        result = subtract(nums)
    elif el == "+":
        result = add(nums)
    elif el == "*":
        result = multiply(nums)
    elif el == "/":
        result = divide(nums)
    nums = deque([result])

print(result)