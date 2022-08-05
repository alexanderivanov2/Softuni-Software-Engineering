class dictionary_iter:
    def __init__(self, dict_iter):
        self.dict_iter = dict_iter
        self.data = [(key, value) for (key, value) in self.dict_iter.items()]
        self.i = 0
        self.n = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        temp = self.data[self.i]
        self.i += 1
        return temp

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)