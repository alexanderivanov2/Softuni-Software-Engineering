import unittest
from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("A")

    def test_constructor(self):
        self.assertEqual("A", self.student.name)
        self.assertTrue(isinstance(self.student.courses, dict))
        # second
        self.student_2 = Student("A", {"abc": ["ABC"]})
        self.assertEqual({"abc": ["ABC"]}, self.student_2.courses)

    def test_enroll_when_course_exist(self):
        self.student.courses.update({"abc": ["A"]})
        result = self.student.enroll("abc", ["B"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"abc": ["A", "B"]}, self.student.courses)

    def test_course_not_exist_and_have_notes(self):
        result = self.student.enroll("A", ["B"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual({"A": ["B"]}, self.student.courses)
        self.student.enroll("B", ["B"])
        self.assertEqual({"A": ["B"], "B": ["B"]}, self.student.courses)

    def test_course_and_notes_doesnt_exist(self):
        result = self.student.enroll("A", ["a"], "B")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"A": []}, self.student.courses)

    def test_add_notes(self):
        self.student.courses.update({"abc": ["A"]})
        result = self.student.add_notes("abc", "B")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"abc": ["A", "B"]}, self.student.courses)

    def test_invalid_add_notes(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("abc", "A")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.student.courses.update({"abc": ["A"]})
        result = self.student.leave_course("abc")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_invalid_leave_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("abc")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
