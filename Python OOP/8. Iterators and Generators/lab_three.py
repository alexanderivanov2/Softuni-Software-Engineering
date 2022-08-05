class vowels:
    def __init__(self, txt):
        self.txt = txt
        self.index = 0
        self.end = len(txt)
        self.vowels = "aeouiy"

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index < self.end:
                el = self.txt[self.index]
                self.index += 1
                if el.lower() in self.vowels:
                    return el
            else:
                raise StopIteration()

#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)


import unittest

class VowelsTests(unittest.TestCase):
    def test_zero(self):
        result = ""
        my_string = vowels('Abcedifuty0o')
        for char in my_string:
            if char.lower() in ['a', 'e', 'i', 'u', 'y', 'o']:
                result += char + "\n"
        self.assertEqual(result, "A\ne\ni\nu\ny\no\n")

if __name__ == '__main__':
    unittest.main()