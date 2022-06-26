class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliters):
        if self.quantity + milliters > self.size:
            return self.quantity
        self.quantity += milliters
        return self.quantity

    def status(self):
        return self.size - self.quantity


# cup = Cup(100, 50)
# cup.fill(50)
# cup.fill(10)
# print(cup.status())

import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        cup = Cup(15, 5)
        self.assertEqual(cup.quantity, 5)
        self.assertEqual(cup.size, 15)

    def test_fill_success(self):
        cup = Cup(10, 5)
        cup.fill(3)
        self.assertEqual(cup.quantity, 8)

    def test_fill_error(self):
        cup = Cup(100, 100)
        cup.fill(1)
        self.assertEqual(cup.quantity, 100)

    def test_status_no_change(self):
        cup = Cup(10, 4)
        self.assertEqual(cup.status(), 6)

    def test_status_changed(self):
        cup = Cup(10, 5)
        cup.fill(3)
        self.assertEqual(cup.status(), 2)


if __name__ == "__main__":
    unittest.main()