import unittest

from exam_3_test.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.a = Train("A", 2,)

    def test_create(self):
        self.assertEqual(self.a.name, "A")
        self.assertEqual(self.a.capacity, 2)
        self.assertEqual(self.a.passengers, [])

    def test_add_passenger(self):
        result = self.a.add("A")
        self.assertEqual("Added passenger A", result)
        with self.assertRaises(ValueError) as ex:
            self.a.add("A")
        self.assertEqual("Passenger A Exists", str(ex.exception))
        self.a.add("B")
        with self.assertRaises(ValueError) as ex:
            self.a.add("C")
        self.assertEqual("Train is full", str(ex.exception))

    def test_remove(self):
        self.a.add("B")
        result = self.a.remove("B")
        self.assertEqual("Removed B", result)
        with self.assertRaises(ValueError) as ex:
            self.a.remove("B")
        self.assertEqual("Passenger Not Found",str(ex.exception))

if __name__ == "__main__":
    unittest.main()