class vowels:
    def __init__(self, string):
        self.string = string
        self.i = 0
        self.end = len(string) - 1
        self.vowels = ["A", "a", "E", "e", "I", "i", "U", "u", "Y", "y", "O", "o"]

    def __iter__(self):
        return self

    def __next__(self):

        if self.i <= self.end:
            result = self.string[self.i]
            while result not in self.vowels and self.i < self.end:
                self.i += 1
                result = self.string[self.i]
            self.i += 1
            return result
        else:
            raise StopIteration



my_string = vowels("Abcedifuty0o")
for char in my_string:
    print(char)