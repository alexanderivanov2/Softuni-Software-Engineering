def possible_permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in possible_permutations(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


# test zero
import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        result = possible_permutations([1, 2, 3])
        self.assertEqual(next(result), [1, 2, 3])
        self.assertEqual(next(result), [1, 3, 2])
        self.assertEqual(next(result), [2, 1, 3])
        self.assertEqual(next(result), [2, 3, 1])
        self.assertEqual(next(result), [3, 1, 2])
        self.assertEqual(next(result), [3, 2, 1])

if __name__ == '__main__':
    unittest.main()