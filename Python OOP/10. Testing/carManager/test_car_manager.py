import unittest
from car_manager import Car


# car = Car("a", "b", 1, 4)
# car.make = ""

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car("a", "b", 1, 5)

    def test_constructor_make(self):
        self.assertEqual("a", self.car.make)
        self.assertEqual("b", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(5, self.car.fuel_capacity)

    def test_invalid_make(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_invalid_model(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_invalid_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_invalid_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_invalid_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel(self):
        self.car.refuel(5)
        self.assertEqual(5, self.car.fuel_amount)

    def test_refuel_with_more_than_capacity(self):
        self.car.refuel(7)
        self.assertEqual(5, self.car.fuel_amount)

    def test_refuel_with_negative_fuel_or_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive(self):
        self.car.fuel_amount = 5
        self.car.drive(100)
        self.assertEqual(4, self.car.fuel_amount)

    def test_over_maximum_distance(self):
        self.car.fuel_amount = 5
        with self.assertRaises(Exception) as ex:
            self.car.drive(700)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
