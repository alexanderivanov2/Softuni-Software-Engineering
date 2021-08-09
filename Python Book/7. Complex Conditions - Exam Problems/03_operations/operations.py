n1 = int(input())
n2 = int(input())
operator = input()

operator1 = ""
result = 0
even_odd = 0
zero = f"Cannot divide {n1} by zero"

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = n1 + n2
        even_odd = result % 2
    elif operator == "-":
        result = n1 - n2
        even_odd = result % 2
    else:
        result = n1 * n2
        even_odd = result % 2
elif operator == "/" or operator == "%":
    if n1 == 0 or n2 == 0:
        zero
    elif operator == "/":
        result = n1 / n2
    elif operator == "%":
        result = n1 % n2

if operator == "+" or operator == "-" or operator == "*":
    if even_odd == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == "/" or operator == "%":
    if n1 == 0 or n2 == 0:
        print(zero)
    elif operator == "%":
        print(f"{n1} % {n2} = {result}")
    else:
        print(f"{n1} / {n2} = {result:.2f}")



