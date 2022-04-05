def calculated_factorial(current_num):
    result = 1
    for i in range(current_num, 0, -1):
        result *= i
    return result


num = int(input())
num_2 = int(input())
result_one = calculated_factorial(num)
result_two = calculated_factorial(num_2)
print(f"{result_one / result_two:.2f}")