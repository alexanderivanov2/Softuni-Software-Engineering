def calculates(action, a, b):
    if action =="subtract":
        return a - b
    elif action == "add":
        return a + b
    elif action == "multiply":
        return a * b
    elif action == "divide":
        return a // b


sign = input()
num_1 = int(input())
num_2 = int(input())

print(calculates(sign, num_1, num_2))