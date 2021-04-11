n = int(input())

sequence = []

for i in range(n):
    sequence.append(int(input()))

print(f"Max number: {max(sequence)}\nMin number: {min(sequence)}")
