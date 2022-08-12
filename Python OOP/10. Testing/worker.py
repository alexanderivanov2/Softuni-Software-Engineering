import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."

import unittest


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Al", 9000, 100)

    def test_initialized_name(self):
        name = self.worker.name
        expect_name = "Al"
        self.assertEqual(name, expect_name)

    def test_initialized_salary(self):
        salary = self.worker.salary
        expect_salary = 9000
        self.assertEqual(salary, expect_salary)

    def test_initialized_energy(self):
        energy = self.worker.energy
        expect_energy = 100
        self.assertEqual(energy, expect_energy)

    def test_rest_method_working(self):
        self.worker.rest()
        after_rest_energy = self.worker.energy
        expect_rest_energy = 101
        self.assertEqual(after_rest_energy, expect_rest_energy)

    def test_error_raise_if_worker_try_work_with_zero(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_error_raises_if_worker_try_work_with_less_than_zero(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_correctly_raised_salary_after_work(self):
        self.worker.work()
        expect_money = 9000
        self.assertEqual(self.worker.money, expect_money)

    def test_worker_energy_get_down_after_work(self):
        self.worker.work()
        expect_energy = 99
        self.assertEqual(self.worker.energy, expect_energy)

    def test_get_info_method(self):
        get_info = self.worker.get_info()
        expect_info = f'Al has saved 0 money.'
        self.assertEqual(get_info, expect_info)


if __name__ == "__main__":
    unittest.main()
