from collections import deque

expression = deque([el for el in input()])

opened = ["[", "{", "("]
closed = ["]", "}", ")"]

opened_stack = []
balanced = True

if len(expression) % 2 == 0:
    while expression:
        parentheses = expression.popleft()
        if parentheses in opened:
            opened_stack.append(parentheses)
        elif parentheses in closed:
            open_parentheses = opened_stack.pop()
            if parentheses == ")" and open_parentheses == "(":
                continue
            elif parentheses == "]" and open_parentheses == "[":
                continue
            elif parentheses == "}" and open_parentheses == "{":
                continue
            else:
                balanced = False
                break
else:
    balanced = False

if balanced:
    print("YES")
else:
    print("NO")