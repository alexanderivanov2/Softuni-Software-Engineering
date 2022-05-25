n = int(input())
even = set()
odd = set()

for _ in range(1, n + 1):
    word_ord = [ord(x) for x in input()]
    if _ == 0:
        final_sum = sum(word_ord) // 1
    else:
        final_sum = sum(word_ord) // _
    if final_sum % 2 == 0:
        even.add(final_sum)
    else:
        odd.add(final_sum)

sum_odd = sum(odd)
sum_even = sum(even)
if sum_odd == sum_even:
    print_num = tuple(even.union(odd))
    print(", ".join(str(x) for x in print_num))
elif sum_odd > sum_even:
    print_num = tuple(odd.difference(even))
    print(", ".join(str(x) for x in print_num))
elif sum_even > sum_odd:
    print_num = tuple(even.symmetric_difference(odd))
    print(", ".join(str(x) for x in print_num))
