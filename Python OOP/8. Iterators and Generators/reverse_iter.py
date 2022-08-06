class reverse_iter:
    def __init__(self, list_nums):
        self.list_nums = list_nums
        self.i = len(list_nums) - 1
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            result = self.list_nums[self.i]
            self.i -= 1
            return result
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)