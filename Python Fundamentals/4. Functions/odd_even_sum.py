def get_odd_even_sum(num):
    odd = [int(el) for el in num if not int(el) % 2 == 0]
    even = [int(el) for el in num if int(el) % 2 == 0]
    return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"


num = str(int(input()))
print(get_odd_even_sum(num))
