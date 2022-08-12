import unittest
from extended_list import IntegerList


class IntegerListTest(unittest.TestCase):
    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3)

    def test_constructor(self):
        self.integer_list = IntegerList(1, [2, 3], "@", True, 2, 3, "777", 4)
        expect_result = [1, 2, 3, 4]
        self.assertEqual(expect_result, self.integer_list.get_data())

    def test_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_element(self):
        self.integer_list.add(4)
        expect_result = [1, 2, 3, 4]
        self.assertEqual(expect_result, self.integer_list.get_data())

    def test_add_not_integer_in_list(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add("A")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index(self):
        self.integer_list.remove_index(0)
        self.assertEqual([2, 3], self.integer_list.get_data())

    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(5)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get(self):
        get_element = self.integer_list.get(1)
        self.assertEqual(2, get_element)

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert(self):
        self.integer_list.insert(1, 7)
        actual_index = self.integer_list.get_data()
        self.assertEqual(7, actual_index[1])

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(3, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(2, "A")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest(self):
        big = 3
        get_big = self.integer_list.get_biggest()
        self.assertEqual(big, get_big)

    def test_get_index(self):
        index = 1
        get_index = self.integer_list.get_index(2)
        self.assertEqual(index, get_index)


if __name__ == "__main__":
    unittest.main()
