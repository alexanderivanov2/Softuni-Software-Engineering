class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return float(f"{Circle.pi * pow(self.radius, 2):.2f}")

    def get_circumference(self):
        return float(f"{2 * Circle.pi * self.radius:.2f}")


import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        c = Circle(15)
        self.assertEqual(c.radius, 15)

    def test_class_attributes(self):
        self.assertEqual(Circle.pi, 3.14)

    def test_set_radius(self):
        c = Circle(15)
        c.set_radius(160)
        self.assertEqual(c.radius, 160)

    def test_get_area(self):
        c = Circle(4)
        self.assertEqual(c.get_area(), 50.24)

    def test_get_circumference(self):
        c = Circle(11)
        self.assertEqual(c.get_circumference(), 69.08)


if __name__ == "__main__":
    unittest.main()