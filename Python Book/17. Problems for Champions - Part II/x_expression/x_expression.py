import math
expression = input()
symbols = list(expression)
symbol = symbols.pop(0)
result = 0
expression_operator = "+"
inner_operator = "+"
inner_result = 0

while symbol != "=":
    if symbol == "(":
        inner_result = 0
        inner_operator = "+"
        while symbol != ")":
            symbol = symbols.pop(0)
            if 49 <= ord(symbol) <= 57:
                if inner_operator == "+":
                    inner_result += ord(symbol) - ord("0")
                elif inner_operator == "-":
                    inner_result -= ord(symbol) - ord("0")
                elif inner_operator == "/":
                    inner_result /= ord(symbol) - ord("0")
                elif inner_operator == "*":
                    inner_result *= ord(symbol) - ord("0")
            elif symbol == "+" or symbol == "-" or symbol == "/" or symbol == "*":
                inner_operator = symbol
        if expression_operator == "+":
            result += inner_result
        elif expression_operator == "-":
            result -= inner_result
        elif expression_operator == "/":
            result /= inner_result
        elif expression_operator == "*":
            result *= inner_result
    elif 49 <= ord(symbol) <= 57:
        if expression_operator == "+":
            result += ord(symbol) - ord("0")
        elif expression_operator == "-":
            result -= ord(symbol) - ord("0")
        elif expression_operator == "/":
            result /= ord(symbol) - ord("0")
        elif expression_operator == "*":
            result *= ord(symbol) - ord("0")
    elif symbol == "+" or symbol == "-" or symbol == "/" or symbol == "*":
        expression_operator = symbol
    symbol = symbols.pop(0)

print(f"{result:.2f}")