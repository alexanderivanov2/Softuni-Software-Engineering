from exam_4_test.student_report_card import StudentReportCard
import unittest


class TestStudentReportCard(unittest.TestCase):
    def setUp(self):
        self.example = StudentReportCard("A", 2)

    def test_creation(self):
        self.assertEqual("A", self.example.student_name)
        self.assertEqual(2, self.example.school_year)
        with self.assertRaises(ValueError) as ex:
            self.a = StudentReportCard("", 2)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.a = StudentReportCard("A", 16)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))
        self.assertEqual({}, self.example.grades_by_subject)

    def test_add_grade(self):
        self.example.add_grade("Math", 6)
        self.assertEqual({"Math": [6]}, self.example.grades_by_subject)
        self.example.add_grade("Math", 6)
        self.assertEqual({"Math": [6, 6]}, self.example.grades_by_subject)

    def test_average_grade(self):
        self.example.add_grade("Math", 6)
        self.example.add_grade("Math2", 6)
        result = self.example.average_grade_by_subject()
        self.assertEqual("Math: 6.00\nMath2: 6.00", result)

    def test_average_grade_all(self):
        self.example.add_grade("Math", 6)
        self.example.add_grade("Math", 6)
        self.example.add_grade("Math2", 6)
        result = self.example.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 6.00", result)

    def test_repr(self):
        self.example.add_grade("Math", 6)
        self.example.add_grade("Math", 6)
        self.example.add_grade("Math2", 6)
        message = "Name: A\nYear: 2\n----------\nMath: 6.00\nMath2: 6.00\n----------\nAverage Grade: 6.00"
        result = self.example.__repr__()
        self.assertEqual(message, result)

    def test_empty(self):
        result = self.example.average_grade_by_subject()
        self.assertEqual("", result)
        with self.assertRaises(ZeroDivisionError) as ex:
            self.example.average_grade_for_all_subjects()
        self.assertEqual("division by zero", str(ex.exception))



if __name__ == "__main__":
    unittest.main()
