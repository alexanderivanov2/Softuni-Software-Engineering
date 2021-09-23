import math

n = int(input())
stars = "*"
down_line = "-"
sides = "|"

roof = math.ceil(n / 2)
floors = n - roof

print(down_line * (roof - 1), end="")
if n % 2 == 0:
    print(stars * 2, end="")
else:
    print(stars, end="")
print(down_line * (roof - 1))

if not n % 2 == 0:
    for middle_of_the_roof_odd in range(2, roof):
        print(down_line * (roof - middle_of_the_roof_odd), end="")
        print(stars * (middle_of_the_roof_odd * 2 - 1), end="")
        print(down_line * (roof - middle_of_the_roof_odd))
else:
    for middle_of_the_roof_even in range(2, roof):
        print(down_line * (roof - middle_of_the_roof_even), end="")
        print(stars * (middle_of_the_roof_even * 2), end="")
        print(down_line * (roof - middle_of_the_roof_even))

if n < 3:
    print("",end="")
else:
    print(stars * n)

for house_floor in range(1, floors + 1):
    print(sides, end="")
    print(stars * (n - 2), end="")
    print(sides)
