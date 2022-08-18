import unittest
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.pf = PaintFactory("A", 5)

    def test_constructor(self):
        self.assertEqual("A", self.pf.name)
        self.assertEqual(5, self.pf.capacity)

    def test_add_ingredient(self):
        self.pf.add_ingredient("green", 2)
        self.assertEqual(2, self.pf.ingredients["green"])
        self.assertTrue("green" in self.pf.ingredients)

    def test_add_ingredient_with_invalid_quantity(self):
        with self.assertRaises(ValueError) as ex:
            self.pf.add_ingredient("green", 6)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_with_invalid_product_type(self):
        with self.assertRaises(TypeError) as ex:
            self.pf.add_ingredient("saf", 6)
        self.assertEqual(f"Ingredient of type saf not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredients(self):
        self.pf.ingredients["white"] = 2
        self.pf.remove_ingredient("white", 1)
        self.assertEqual(1, self.pf.ingredients["white"])

    def test_remove_ingredients_with_invalid_quantity(self):
        self.pf.ingredients["white"] = 2
        with self.assertRaises(ValueError) as ex:
            self.pf.remove_ingredient("white", 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredients_with_invalid_type(self):
        with self.assertRaises(KeyError) as ex:
            self.pf.remove_ingredient("g", 2)
        self.assertEqual(f"\'No such ingredient in the factory\'", str(ex.exception))

    def test_property_products(self):
        self.pf.ingredients["blue"] = 2
        self.assertEqual({"blue": 2}, self.pf.ingredients)


if __name__ == "__main__":
    unittest.main()
