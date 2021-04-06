end_of_loop = int(input())

print_even_powered_by_2 = [print(2 ** x) for x in range(end_of_loop + 1) if x % 2 == 0]

# for i in range(end_of_loop + 1):
#     if i % 2 == 0:
#         print(2 ** i)
