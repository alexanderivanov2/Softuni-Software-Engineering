tribonacci_first = int(input())
tribonacci_second = int(input())
tribonacci_third = int(input())
spiral_current = int(input())
spiral_step = int(input())
tribonacci_numbers = [tribonacci_first, tribonacci_second, tribonacci_third]
tribonacci_current = tribonacci_third

while tribonacci_current < 1000000:
    tribonacci_current = tribonacci_first + tribonacci_second + tribonacci_third
    tribonacci_numbers.append(tribonacci_current)
    tribonacci_first = tribonacci_second
    tribonacci_second = tribonacci_third
    tribonacci_third = tribonacci_current


spiral_numbers = [spiral_current]
spiral_count = 0
spiral_step_mul = 1