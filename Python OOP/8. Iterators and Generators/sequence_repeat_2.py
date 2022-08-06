class sequence_repeat:
    def __init__(self, txt, count):
        self.txt = txt
        self.count = count
        self.index = 0
        self.txt_len = len(txt)

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > 0:
            if self.index == self.txt_len:
                self.index = 0
            value = self.txt[self.index]
            self.index += 1
            self.count -= 1
            return value
        raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')