number = int(input())
first_part = ""
first_part1 = ""
second_part = ""
if number <= 19:
    first_part1 = number
elif 20 <= number <= 99:
    first_part = number // 10
    second_part = number % 10
elif 100 >= number:
    print("one hundred")

if first_part1 == 0:
    first_part1 = "zero"
elif first_part1 == 1:
    first_part1 = "one"
elif first_part1 == 2:
    first_part1 = "two"
elif first_part1 == 3:
    first_part1 = "three"
elif first_part1 == 4:
    first_part1 = "four"
elif first_part1 == 5:
    first_part1 = "five"
elif first_part1 == 6:
    first_part1 = "six"
elif first_part1 == 7:
    first_part1 = "seven"
elif first_part1 == 8:
    first_part1 = "eight"
elif first_part1 == 9:
    first_part1 = "nine"
elif first_part1 == 10:
    first_part1 = "ten"
elif first_part1 == 11:
    first_part1 = "eleven"
elif first_part1 == 12:
    first_part1 = "twelve"
elif first_part1 == 13:
    first_part1 = "thirteen"
elif first_part1 == 14:
    first_part1 = "fourteen"
elif first_part1 == 15:
    first_part1 = "fifteen"
elif first_part1 == 16:
    first_part1 = "sixteen"
elif first_part1 == 17:
    first_part1 = "seventeen"
elif first_part1 == 18:
    first_part1 = "eighteen"
elif first_part1 == 19:
    first_part1 = "nineteen"

if first_part == 2:
    first_part = "twenty"
elif first_part == 3:
    first_part = "thirty"
elif first_part == 4:
    first_part = "forty"
elif first_part == 5:
    first_part = "fifty"
elif first_part == 6:
    first_part = "sixty"
elif first_part == 7:
    first_part = "seventy"
elif first_part == 8:
    first_part = "eighty"
elif first_part == 9:
    first_part = "ninety"

if second_part == 1:
    second_part = "one"
elif second_part == 2:
    second_part = "two"
elif second_part == 3:
    second_part = "three"
elif second_part == 4:
    second_part = "four"
elif second_part == 5:
    second_part = "five"
elif second_part == 6:
    second_part = "six"
elif second_part == 7:
    second_part = "seven"
elif second_part == 8:
    second_part = "eight"
elif second_part == 9:
    second_part = "nine"

if second_part == 0:
    print(first_part)
elif 20 <= number < 100:
    print(f"{first_part} {second_part}")
elif 20 > number:
    print(first_part1)
