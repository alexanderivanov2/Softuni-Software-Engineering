def number_definer(n):
    result = ""
    if n == 0:
        result = "zero"
    elif 1 > n > 0:
        result = "small positive"
    elif 1 < n < 1_000_000:
        result = "positive"
    elif n > 1_000_000:
        result = "large positive"
    elif -1 < n < 0:
        result = "small negative"
    elif -1 > n > -1_000_000:
        result = "negative"
    elif n < -1_000_000:
        result = "large negative"
    return result


print(number_definer(float(input())))
