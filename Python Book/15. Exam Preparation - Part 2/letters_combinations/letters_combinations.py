start = ord(input())
end = ord(input())
exception = ord(input())
count = 0
for a in range(start, end + 1):
    for b in range(start, end + 1):
        for c in range(start, end + 1):
            if a != exception and b != exception and c != exception:
                count += 1
                print(f"{chr(a)}{chr(b)}{chr(c)}", end=" ")
print(count)