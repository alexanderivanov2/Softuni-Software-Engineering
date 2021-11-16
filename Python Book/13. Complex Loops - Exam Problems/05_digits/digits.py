n = int(input())

n1 = (n // 100) % 10
n2 = (n // 10) % 10
n3 = n % 10

end_num = n
rows = n1 + n2
number_on_rows = n1 + n3

for row in range(1, rows + 1):
    for num_on_rows in range(1, number_on_rows + 1):
        if end_num % 5 == 0:
            end_num = end_num - n1
        elif end_num % 3 == 0:
            end_num = end_num - n2
        else:
            end_num = end_num + n3
        print(end_num, end=" ")
    print()