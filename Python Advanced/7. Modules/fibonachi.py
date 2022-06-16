def get_result(n, find):
    fibonachi = [0, 1, 1]
    while not len(fibonachi) == n:
        new_number = fibonachi[-1] + fibonachi[-2]
        fibonachi.append(new_number)
    print(*[el for el in fibonachi])
    if find in fibonachi:
        print(f"The number - {find} is at index {fibonachi.index(find)}")
    else:
        print(f"The number {find} is not in the sequence")



