n = int(input())
previsious_sum = 0
current_sum = 0
diff = 0
maxdiff = 0

for i in range(n):
    num1 = int(input())
    num2 = int(input())
    curent_sum = num1 + num2
    diff = abs(curent_sum - previsious_sum)
    previsious_sum = curent_sum

if n <= 1:
    print(f"Yes, value = {diff}")
elif diff == 0:
    print(f"Yes, value = {previsious_sum}")
else:
    print(f"No, maxdiff = {diff}")