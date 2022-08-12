import unittest


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception("Already fed.")
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception("Cannot sleep while hungry")
        self.sleepy = False

import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Penny")

    def test_increasing_size_and_sleepy_status_after_eating(self):
        self.cat.eat()
        current_size = self.cat.size
        expected_size = 1
        sleepy = self.cat.sleepy
        expect_sleepy_status = True
        self.assertEqual(expected_size, current_size)
        self.assertEqual(expect_sleepy_status, sleepy)

    def test_trying_to_feed_after_eating(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_fall_asleep_without_feeding(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))


    def test_sleepy_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()