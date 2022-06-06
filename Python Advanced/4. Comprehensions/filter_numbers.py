start = int(input())
end = int(input())

comprehension = [num for num in range(start, end + 1) if any(num % i == 0 for i in range(2, 11))]
print(comprehension)