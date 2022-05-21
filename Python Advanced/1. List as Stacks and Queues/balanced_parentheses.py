opening = ["(", "[", "{"]
close = [")", "]", "}"]

line = input()
stack = []
for el in line:
    if el in opening:
        stack.append(el)
    elif el in close and len(stack) == 0:
        print("NO")
        exit()
    else:
        last = stack.pop()
        if last == "{" and el == "}":
            continue
        elif last == "[" and el == "]":
            continue
        elif last == "(" and el == ")":
            continue
        else:
            print("NO")
            exit()

if stack:
    print("NO")
else:
    print("YES")
