def calculate_combo(names, n, combs=[]):
    if len(combs) == n:
        print(", ".join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        calculate_combo(names[i+1:], n, combs)
        combs.pop()


names = input().split(", ")
n = int(input())

calculate_combo(names, n)
