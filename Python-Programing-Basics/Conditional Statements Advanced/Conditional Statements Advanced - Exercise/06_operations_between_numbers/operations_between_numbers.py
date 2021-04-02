def get_even_or_odd(res):
    if res % 2 == 0:
        return "even"
    else:
        return "odd"


number_one = int(input())
number_two = int(input())
operator = input()
operator_string = ["+", "-", "*", "/", "%"]

if operator == "+":
    result = number_one + number_two
    even_or_odd = get_even_or_odd(result)
    print(f"{number_one} {operator} {number_two} = {result} - {even_or_odd}")
elif operator == "-":
    result = number_one - number_two
    even_or_odd = get_even_or_odd(result)
    print(f"{number_one} {operator} {number_two} = {result} - {even_or_odd}")
elif operator == "*":
    result = number_one * number_two
    even_or_odd = get_even_or_odd(result)
    print(f"{number_one} {operator} {number_two} = {result} - {even_or_odd}")
elif operator == "/":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one / number_two
        print(f"{number_one} / {number_two} = {result:.2f}")
elif operator == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two
        print(f"{number_one} % {number_two} = {result}")
