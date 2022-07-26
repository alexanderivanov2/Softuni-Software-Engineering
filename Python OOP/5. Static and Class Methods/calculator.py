from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce((lambda x, y: x * y), args)

    @staticmethod
    def divide(*args):
        result = args[0]
        for el in args[1:]:
            result /= el
        return result

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
