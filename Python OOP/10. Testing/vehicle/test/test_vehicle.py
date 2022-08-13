import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(5.5, 7.7)

    def test_constructor(self):
        self.assertEqual(5.5, self.vehicle.fuel)
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertEqual(5.5, self.vehicle.capacity)
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertEqual(7.7, self.vehicle.horse_power)
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))

    def test_drive(self):
        self.vehicle.drive(1)
        expected_fuel = 5.5 - 1.25
        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_invalid_drive(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.drive(1)
        self.vehicle.refuel(1.25)
        self.assertEqual(5.5, self.vehicle.fuel)

    def test_invalid_refuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected_str = "The vehicle has 7.7 horse power with 5.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_str, self.vehicle.__str__())

if __name__ == "__main__":
    unittest.main()