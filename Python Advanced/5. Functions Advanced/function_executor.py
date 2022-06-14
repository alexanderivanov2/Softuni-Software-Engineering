def func_executor(*args):
    return [get_result(tup[0], tup[1]) for tup in args]


def get_result(func, args):
    return func(*args)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
