class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.length_of_sequence = len(self.sequence)
        self.index = 0
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.number:
            raise StopIteration
        temp = self.sequence[self.index]
        self.index = self.index + 1 if self.index + 1 < self.length_of_sequence else 0
        self.i += 1
        return temp

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

