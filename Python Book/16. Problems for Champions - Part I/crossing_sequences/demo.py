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

while spiral_current < 1000000:
    spiral_current += spiral_step * spiral_step_mul
    spiral_numbers.append(spiral_current)
    spiral_count += 1
    if spiral_count % 2 == 0:
        spiral_step_mul += 1

found = False
for i in range(0, len(tribonacci_numbers)):
    for j in range(0, len(spiral_numbers)):
        if tribonacci_numbers[i] == spiral_numbers[j] and tribonacci_numbers[i] <= 1000000:
            print(tribonacci_numbers[i])
            found = True
    if found:
        break

if not found:
    print("No")