from math import floor
from itertools import tee


class Integer:
    def __init__(self, value:int):
        self.value = value

    @classmethod
    def from_float(cls,value):
        if not type(value) == float:
            return "value is not a float"
        value = floor(value)
        return cls(value)

    @classmethod
    def from_roman(cls, value):
        numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        cur, prev = tee(numerals[c] for c in reversed(value.upper()))
        result = next(cur) + sum((cur, -cur)[cur < prev] for cur, prev in zip(cur, prev))
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not type(value) == str:
            return "wrong type"
        return cls(int(value))

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        self.value += integer.value
        return self.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))

# import unittest
#
#
# class IntegerTests(unittest.TestCase):
#     def test_basic_init(self):
#         integer = Integer(1)
#         self.assertEqual(integer.value, 1)
#
#     def test_from_float_success(self):
#         integer = Integer.from_float(2.5)
#         self.assertEqual(integer.value, 2)
#
#     def test_from_float_wrong_type(self):
#         result = Integer.from_float("2.5")
#         self.assertEqual(result, "value is not a float")
#
#     def test_from_roman(self):
#         integer = Integer.from_roman("XIX")
#         self.assertEqual(integer.value, 19)
#
#     def test_from_string_success(self):
#         integer = Integer.from_string("10")
#         self.assertEqual(integer.value, 10)
#
#     def test_from_string_wrong_type(self):
#         result = Integer.from_string(1.5)
#         self.assertEqual(result, "wrong type")
#
#
# if __name__ == "__main__":
#     unittest.main()