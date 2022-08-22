from exam_2_test.pet_shop import PetShop
import unittest


class TestPetShop(unittest.TestCase):
    def setUp(self):
        self.pet_shop = PetShop("A")

    def test_add_food(self):
        result = self.pet_shop.add_food("A", 1)
        self.assertEqual("Successfully added 1.00 grams of A.", result)
        self.assertEqual({"A": 1}, self.pet_shop.food)
        result = self.pet_shop.add_food("A", 3)
        self.assertEqual("Successfully added 3.00 grams of A.", result)
        self.assertEqual({"A": 4}, self.pet_shop.food)
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("A", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_pet(self):
        result = self.pet_shop.add_pet("A")
        self.assertEqual("Successfully added A.", result)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("A")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("A", "A")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))
        self.pet_shop.add_pet("A")
        result = self.pet_shop.feed_pet("A", "A")
        self.assertEqual('You do not have A', result)

    def test_feed_pet_2(self):
        self.pet_shop.add_pet("A")
        self.pet_shop.add_food("A", 10)
        result = self.pet_shop.feed_pet("A", "A")
        self.assertEqual("Adding food...", result)
        self.assertEqual(1010, self.pet_shop.food["A"])
        result = self.pet_shop.feed_pet("A", "A")
        self.assertEqual("A was successfully fed", result)
        self.assertEqual(910, self.pet_shop.food["A"])

    def test_repr(self):
        self.pet_shop.add_pet("A")
        expected = 'Shop A:\nPets: A'
        self.assertEqual(expected, repr(self.pet_shop))
        self.pet_shop.add_pet("B")
        expected = 'Shop A:\nPets: A, B'
        self.assertEqual(expected, repr(self.pet_shop))

if __name__ == "__main__":
    unittest.main()
