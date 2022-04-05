def sum_numbers(a, b):
    return a + b


def subtract(sum_nums, c):
    return sum_nums - c


a = int(input())
b = int(input())
c = int(input())

sum_nums = sum_numbers(a, b)
print(subtract(sum_nums, c))