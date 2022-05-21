expression = input()

open_brackets = []

for i in range(len(expression)):
    if expression[i] == "(":
        open_brackets.append(i)
    elif expression[i] == ")":
        end_bracket = i + 1
        start_bracket = open_brackets.pop()
        print(f"{expression[start_bracket:end_bracket]}")