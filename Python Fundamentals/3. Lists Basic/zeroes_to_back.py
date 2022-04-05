first_list = input().split(", ")
zero_back_list = [int(el) for el in first_list if int(el) != 0]
zeroes = first_list.count("0")

for i in range(zeroes):
    zero_back_list.append(0)

print(zero_back_list)