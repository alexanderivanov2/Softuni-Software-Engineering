from decimal import Decimal as Dec

money_have = Dec(input())
word = input()
purchace = 0
total = money_have
expenses = 0

while word != "mall.Enter":
    word = input()

word = input()

while word != "mall.Exit":
    for digit in word:
        chr1 = ord(digit)

        if 65 <= chr1 <= 90:
            expenses = Dec(chr1 * 0.5)
        elif 97 <= chr1 <= 122:
            expenses = Dec(chr1 * 0.3)
        elif chr1 == 37:
            expenses = Dec(total / 2)
        elif chr1 == 42:
            total = total + 10
        else:
            expenses = Dec(chr1)

        if expenses <= total and expenses != 0:
            total = Dec(total - expenses)
            purchace += 1
        expenses = 0
    word = input()

if purchace > 0:
    print(f"{purchace} purchases. Money left: {total:.2f} lv.")
else:
    print(f"No purchases. Money left: {total:.2f} lv.")