number_list = input().split(", ")
result = 1

for i in range(len(number_list)):
    number = int(number_list[i])
    if number <= 5:
        result *= number
    elif 10 >= number > 5:
        result /= number

print(round(result))
