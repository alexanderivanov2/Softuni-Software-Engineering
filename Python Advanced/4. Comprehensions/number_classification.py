numbers = [int(x) for x in input().split(", ")]
positive = []
negative = []
even = []
odd = []
[positive.append(n) if n >= 0 else negative.append(n) for n in numbers]
[even.append(n) if n % 2 == 0 else odd.append(n) for n in numbers]

print(f"Positive: {', '.join(str(num) for num in positive)}")
print(f"Negative: {', '.join(str(num) for num in negative)}")
print(f"Even: {', '.join(str(num) for num in even)}")
print(f"Odd: {', '.join(str(num) for num in odd)}")