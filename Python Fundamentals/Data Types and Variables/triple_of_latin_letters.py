n = int(input())

for i in range(97, 97 + n):
    for i2 in range(97, 97 + n):
        for i3 in range(97, 97 + n):
            print(f"{chr(i)}{chr(i2)}{chr(i3)}")
