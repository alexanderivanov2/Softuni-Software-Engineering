import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.factory = PaintFactory("A", 10)

    def test_create(self):
        self.assertEqual("A", self.factory.name)
        self.assertEqual(10, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_add_ingredient(self):
        self.factory.add_ingredient("blue", 7)
        self.assertEqual({"blue": 7}, self.factory.ingredients)
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("blue", 7)
        self.assertEqual("Not enough space in factory", str(ex.exception))
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("WWW", 7)
        self.assertEqual(f"Ingredient of type WWW not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient(self):
        self.factory.add_ingredient("blue", 7)
        self.factory.remove_ingredient("blue", 5)
        self.assertEqual({"blue": 2}, self.factory.ingredients)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("blue", 5)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("A", 5)
        self.assertEqual('No such ingredient in the factory', str(ex.exception)[1:-1])

    def test_products(self):
        self.factory.add_ingredient("blue", 7)
        self.factory.add_ingredient("green", 2)
        self.assertEqual({'blue': 7, 'green': 2}, self.factory.products)


if __name__ == "__main__":
    unittest.main()