numbers_list = [int(el) for el in input().split(", ")]
even_numbers = [i for i in range(len(numbers_list)) if numbers_list[i] % 2 == 0]

print(even_numbers)