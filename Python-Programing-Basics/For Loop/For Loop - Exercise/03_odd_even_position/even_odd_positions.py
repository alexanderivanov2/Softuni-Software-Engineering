def get_odd_print_statistic(odds):
    if len(odds) == 0:
        return f"OddSum=0.00,\nOddMin=No,\nOddMax=No,"
    else:
        return f"OddSum={sum(odds):.2f},\nOddMin={min(odds):.2f},\nOddMax={max(odds):.2f},"


def get_even_print_statistic(evens):
    if len(evens) == 0:
        return f"\nEvenSum=0.00,\nEvenMin=No,\nEvenMax=No"
    else:
        return f"\nEvenSum={sum(evens):.2f},\nEvenMin={min(evens):.2f},\nEvenMax={max(evens):.2f}"


n = int(input())
even = []
odd = []

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

odd_print = get_odd_print_statistic(odd)
even_print = get_even_print_statistic(even)

print(odd_print, end="")
print(even_print)
