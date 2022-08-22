import unittest
from exam_test.team import Team


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("A")

    def test_name_creation(self):
        self.assertEqual(self.team.name, "A")
        with self.assertRaises(ValueError) as ex:
            Team("A1")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            Team("11")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            Team("")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            Team("A*")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        result = self.team.add_member(**{"A": 1, "B": 2})
        self.assertEqual("Successfully added: A, B", result)
        self.assertEqual(self.team.members, {"A": 1, "B": 2})
        result = self.team.add_member(**{"A": 3})
        self.assertEqual(self.team.members, {"A": 1, "B": 2})
        self.assertEqual("Successfully added: ", result)
        self.team.add_member(**{"C": 3})
        self.assertEqual(self.team.members, {"A": 1, "B": 2, "C": 3})

    def test_remove_member(self):
        self.team.add_member(**{"A": 2, "B": 2})
        result = self.team.remove_member("C")
        self.assertEqual(result, "Member with name C does not exist")
        self.assertEqual({"A": 2, "B": 2}, self.team.members)
        result = self.team.remove_member("B")
        self.assertEqual(result, "Member B removed")
        self.assertEqual({"A": 2}, self.team.members)

    def test_gt(self):
        self.team2 = Team("B")
        result = self.team.__gt__(self.team2)
        self.assertEqual(False, result)
        self.team.add_member(**{"A": 2, "B": 2})
        result = self.team.__gt__(self.team2)
        self.assertEqual(True, result)
        result = self.team2.__gt__(self.team)
        self.assertEqual(False, result)
        self.team2.add_member(**{"A": 2, "B": 2, "C": 3})
        result = self.team2.__gt__(self.team)
        self.assertEqual(True, result)

    def test_len(self):
        self.assertEqual(0, self.team.__len__())
        self.assertEqual(0, len(self.team))
        self.team.add_member(**{"A": 2, "B": 2})
        self.assertEqual(2, self.team.__len__())
        self.assertEqual(2, len(self.team))

    def test_add(self):
        self.team.add_member(**{"A": 2, "B": 2})
        self.team2 = Team("B")
        self.team2.add_member(**{"C": 2, "D": 2})
        result = self.team.__add__(self.team2)
        self.assertEqual({"A": 2, "B": 2, "C": 2, "D": 2}, result.members)

    def test_add_2(self):
        self.team.add_member(**{"A": 2, "B": 2})
        self.team2 = Team("B")
        self.team2.add_member(**{"A": 2, "D": 2})
        result = self.team.__add__(self.team2)
        self.assertEqual({"A": 2, "B": 2, "D": 2}, result.members)
        self.assertEqual("AB", result.name)

    def test_str(self):
        self.team.add_member(**{"A": 2, "B": 72})
        result = str(self.team)
        expected = f"Team name: {self.team.name}\nMember: B - 72-years old\nMember: A - 2-years old"
        self.assertEqual(result, expected)
        self.team.members["B"] = 2
        result = str(self.team)
        expected = f"Team name: {self.team.name}\nMember: A - 2-years old\nMember: B - 2-years old"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
