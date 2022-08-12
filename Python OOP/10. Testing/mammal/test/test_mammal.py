import unittest
from project.mammal import Mammal



class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("A", "AB", "Sound")

    def test_constructor(self):
        self.assertEqual("A", self.mammal.name)
        self.assertEqual("AB", self.mammal.type)
        self.assertEqual("Sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        expected_result = "A makes Sound"
        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        expect = "A is of type AB"
        self.assertEqual(expect, self.mammal.info())


if __name__ == "__main__":
    unittest.main()
