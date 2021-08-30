n = int(input())
min_size_even = 100000000000000
max_size_even = -1000000000000
min_size_odd = 100000000000000
max_size_odd = -1000000000000
sum_odd = 0
sum_even = 0

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        sum_even += num
        if num < min_size_even:
            min_size_even = num
        if num > max_size_even:
            max_size_even = num
    else:
        sum_odd += num
        if num < min_size_odd:
            min_size_odd = num
        if num > max_size_odd:
            max_size_odd = num

if n < 1:
    max_size_odd = "No"
    min_size_odd = "No"
    min_size_even = "No"
    max_size_even = "No"
    print(f"OddSum = {sum_odd:g}\nOddMin = {min_size_odd}\nOddMax = {max_size_odd}\nEvenSum = {sum_even:g}"
          f"\nEvenMin = {min_size_even}\nEvenMax = {max_size_even}")
elif n == 1:
    min_size_even = "No"
    max_size_even = "No"
    print(f"OddSum = {sum_odd:g}\nOddMin = {min_size_odd:g}\nOddMax = {max_size_odd:g}\nEvenSum = {sum_even:g}"
          f"\nEvenMin = {min_size_even}\nEvenMax = {max_size_even}")
else:
    print(f"OddSum = {sum_odd:g}\nOddMin = {min_size_odd:g}\nOddMax = {max_size_odd:g}\nEvenSum = {sum_even:g}"
          f"\nEvenMin = {min_size_even:g}\nEvenMax = {max_size_even:g}")
