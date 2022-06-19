class ValueCannotBeNegativeError(Exception):
    def __init__(self, value):
        super().__init__(f"{value} is negative")

for i in range(1, 6):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegativeError(num)
