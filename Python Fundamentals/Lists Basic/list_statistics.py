n = int(input())
positive = []
negative = []

for i in range(n):
    num = int(input())
    if num < 0:
        negative.append(num)
    else:
        positive.append(num)


print(positive)
print(negative)
print(f"Count of positives: {alen(positive)}. Sum of negatives: {sum(negative)}")