numbers = list(map(int, input().split()))
negative = [el for el in numbers if el < 0]
positive = [el for el in numbers if el >= 0]

print(sum(negative))
print(sum(positive))

if abs(sum(negative)) > sum(positive):
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")