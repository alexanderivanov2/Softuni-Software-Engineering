def create_top(n):
    result = []
    for i in range(1, n + 1):
        result.append("*" * i)
    return result


def create_bottom(n):
    result = []
    for i in range(n - 1, 0, -1):
        result.append("*" * i)
    return result


num = int(input())
print("\n".join(create_top(num)))
print("\n".join(create_bottom(num)))
