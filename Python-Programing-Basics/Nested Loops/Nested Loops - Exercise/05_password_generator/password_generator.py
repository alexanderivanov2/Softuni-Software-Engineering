numbers = int(input())
char = int(input()) + 97

for i in range(1, numbers + 1):
    for i2 in range(1, numbers + 1):
        for i3 in range(97, char):
            for i4 in range(97, char):
                for i5 in range(1, numbers + 1):
                    if i < i5 > i2:
                        print(f"{i}{i2}{chr(i3)}{chr(i4)}{i5}", end=" ")

