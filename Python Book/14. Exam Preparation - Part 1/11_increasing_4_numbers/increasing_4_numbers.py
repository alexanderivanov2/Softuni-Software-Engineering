a = int(input())
b = int(input())
have = True

for n1 in range(a, b + 1):
    for n2 in range(n1 + 1, b + 1):
        for n3 in range(n2 + 1, b + 1):
            for n4 in range(n3 + 1, b + 1):
                if a <= n1 < n2 < n3 < n4 <= b:
                    print(f"{n1} {n2} {n3} {n4}")
                    have = False

if have:
    print("No")
