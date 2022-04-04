n = int(input())
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)

command = input()

if command == "even":
    final = [el for el in nums if el % 2 == 0]
elif command == "odd":
    final = [el for el in nums if el % 2 != 0]
elif command == "positive":
    final = [el for el in nums if el >= 0]
else:
    final = [el for el in nums if el < 0]

print(final)
