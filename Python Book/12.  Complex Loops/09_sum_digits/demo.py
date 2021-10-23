n = int(input())
sum = 0
last_digit = 0

while True:
    last_digit = n % 10
    n = n // 10
    sum = sum + last_digit
    if not 0 < n:
        break

print(sum)