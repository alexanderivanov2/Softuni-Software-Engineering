from collections import deque


def check_sequence(seq):
    while seq:
        s = seq.popleft()
        e = seq.pop()
        if s != e:
            continue
        else:
            return "UNBALANCED"
    return "BALANCED"


n = int(input())
check = "BALANCED"
brackets = deque()

for i in range(n):
    data = input()
    if data in ["(", ")"]:
        brackets.append(data)

if len(brackets) % 2 == 0 and (brackets[0] == "(" and brackets[-1] == ")") and brackets.count("(") == brackets.count(
        ")"):
    sequence = deque()
    while brackets:
        a = brackets.popleft()
        sequence.append(a)
        if len(brackets) > 0:
            if brackets[0] == a:
                check = "UNBALANCED"
                break
        if a == ")" and brackets.count("(") == brackets.count(")"):
            check = check_sequence(sequence)
            sequence = deque()
            if check == "UNBALANCED":
                break

else:
    check = "UNBALANCED"

print(check)
