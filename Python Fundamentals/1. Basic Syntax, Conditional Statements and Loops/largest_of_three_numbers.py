def get_largest_num():
    n = []
    for i in range(3):
        number = int(input())
        n.append(number)
    return max(n)


print(get_largest_num())
