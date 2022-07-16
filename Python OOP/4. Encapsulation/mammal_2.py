class Mammal:
    __kingdom = "animals"

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        m = Mammal("cat", "domestic", "Meow")
        self.assertEqual(m._Mammal__kingdom, "animals")
        self.assertEqual(m.name, "cat")
        self.assertEqual(m.type, "domestic")
        self.assertEqual(m.sound, "Meow")

    def test_make_sound(self):
        m = Mammal("lion", "white", "Roar")
        res = m.make_sound()
        self.assertEqual(res, "lion makes Roar")

    def test_get_kingdom(self):
        m = Mammal("bear", "polar", "Growl")
        res = m.get_kingdom()
        self.assertEqual(res, "animals")

    def test_info(self):
        m = Mammal("bear", "polar", "Growl")
        res = m.info()
        self.assertEqual(res, "bear is of type polar")


if __name__ == "__main__":
    unittest.main()