import unittest
import worker


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = worker.Worker("Al", 9000, 100)

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

    # def test_error_raise_if_worker_try_work_with_zero(self):
    #     self.worker.energy = 0
    #     self.assertRaises(Exception, self.worker.work())
    #     self.assertRaises(Exception, self.worker.work())

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