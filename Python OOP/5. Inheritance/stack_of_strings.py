class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return f'[{", ".join(f"{self.data[i]}" for i in range(len(self.data) - 1, -1, -1))}]'

    def push(self, element):
        if type(element) == str:
            self.data.append(element)

    def pop(self):
        pop_element = self.data.pop()
        return pop_element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if not self.data else False



stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack))
import unittest


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.top(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()