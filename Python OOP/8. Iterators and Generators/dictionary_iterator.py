class dictionary_iter:
    def __init__(self, dict_iter):
        self.dict_iter = dict_iter
        self.curr_key = None
        self.length = len(dict_iter)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count < self.length:
            counter = 0
            for key, value in self.dict_iter.items():
                if counter == self.count:
                    self.count += 1
                    return key, value
                counter += 1
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)