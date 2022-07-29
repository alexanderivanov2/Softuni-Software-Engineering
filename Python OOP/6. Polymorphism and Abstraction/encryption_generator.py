class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        result = ""
        for ch in self.text:
            new_ch = ord(ch) + other
            while new_ch > 126:
                new_ch -= 95

            while new_ch < 32:
                new_ch += 95
            result += chr(new_ch)

        return result

some_text = EncryptionGenerator("I Love Python!")
print(some_text + 1)
print(some_text + (-1))
example = EncryptionGenerator("Super-Secret Message")
print(example + 20)
print(example + (-52))