num1 = int(input())
num2 = int(input())
num3 = int(input())

c = max(num1, num2, num3)
a = min(num1, num2, num3)
b = (num1 + num2 + num3) - (c + a)

if a + b == c:
    print(f"{a} + {b} = {c}")
else:
    print(f"No")