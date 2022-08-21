from exam_1_test.library import Library
import unittest


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.library = Library("A")

    def test_creation(self):
        expected = Library("A")
        self.assertEqual(expected.name, "A")
        self.assertEqual(expected.readers, {})
        self.assertEqual(expected.books_by_authors, {})

    def test_invalid_test_creation(self):
        with self.assertRaises(Exception) as ex:
            Library("")
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book(self):
        self.library.add_book("A", "A")
        self.assertEqual({"A": ["A"]}, self.library.books_by_authors)
        self.library.add_book("A", "A")
        self.assertEqual({"A": ["A"]}, self.library.books_by_authors)
        self.library.add_book("A", "B")
        self.assertEqual({"A": ["A", "B"]}, self.library.books_by_authors)

    def test_reader(self):
        self.library.add_reader("A")
        self.assertEqual({"A": []}, self.library.readers)
        result = self.library.add_reader("A")
        self.assertEqual(f"{'A'} is already registered in the {self.library.name} library.", result)
        # can make_additional_test

    def test_rent_book(self):
        result = self.library.rent_book("A", "A", "A")
        self.assertEqual(f"{'A'} is not registered in the {self.library.name} Library.", result)
        self.library.add_reader("A")
        result = self.library.rent_book("A", "A", "A")
        self.assertEqual(f"{self.library.name} Library does not have any {'A'}'s books.", result)
        self.library.add_book("A", "B")
        result = self.library.rent_book("A", "A", "A")
        self.assertEqual(f"""{self.library.name} Library does not have {"A"}'s "{"A"}".""", result)
        result = self.library.rent_book("A", "A", "B")
        self.assertEqual({"A": [{"A": "B"}]}, self.library.readers)
        self.assertEqual({"A": []}, self.library.books_by_authors)


if __name__ == "__main__":
    unittest.main()
