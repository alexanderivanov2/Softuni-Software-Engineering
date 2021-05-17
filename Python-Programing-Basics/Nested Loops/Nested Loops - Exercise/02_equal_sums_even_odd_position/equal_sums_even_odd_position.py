start_number = int(input())
end_number = int(input())

for num in range(start_number, end_number + 1):
    num = str(num)
    counter = 0
    even = 0
    odd = 0

    for n in num:
        counter += 1
        if counter % 2 == 0:
            even += int(n)
        else:
            odd += int(n)

    if even == odd:
        print(f"{num}", end=' ')