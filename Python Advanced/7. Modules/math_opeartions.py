def get_arguments(text):
    mapper = {"/": divide,
              "*": multiply,
              "-": subtract,
              "+": add_num,
              "^": raise_power}
    n1, sign, n2 = text.split()
    n1 = float(n1)
    n2 = int(n2)
    return print(f"{mapper[sign](n1, n2):.2f}")


def divide(n1, n2):
    result = n1 / n2
    return result


def multiply(n1, n2):
    result = n1 * n2
    return result


def subtract(n1, n2):
    return n1 - n2


def add_num(n1, n2):
    return n1 + n2


def raise_power(n1, n2):
    result = n1 ** n2
    return result




get_arguments(input())
