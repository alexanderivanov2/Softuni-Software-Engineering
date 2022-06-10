numbers = [int(num) for num in input().split()]


def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


even_numbers = list(filter(check_even, numbers))
print(even_numbers)