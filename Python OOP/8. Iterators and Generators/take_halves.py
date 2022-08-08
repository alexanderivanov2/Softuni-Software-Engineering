def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        seq_list = []
        for i in range(1, n + 1):
            seq_list.append(i / 2)
        return seq_list

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
