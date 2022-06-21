def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for i in range(1, n - 1):
        new_row = []
        for i2 in range(len(triangle[i])):
            if i2 == 0:
                new_row.append(triangle[i][i2])
                new_row.append(triangle[i][i2] + triangle[i][i2 + 1])
                continue
            if i2 == len(triangle[i]) - 1:
                new_row.append(triangle[i][i2])
                continue
            new_row.append(triangle[i][i2] + triangle[i][i2 + 1])
        triangle.append(new_row)
    return triangle

import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        actual = get_magic_triangle(5)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

