class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.i = 0
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.count:
            raise StopIteration
        self.i += 1
        temp = self.n
        self.n += self.step
        return temp

numbers = take_skip(10, 5)
for number in numbers:
    print(number)