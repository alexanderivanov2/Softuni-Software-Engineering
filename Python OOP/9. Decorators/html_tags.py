def tags(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, *kwargs)
            res = f"<{tag}>{res}</{tag}>"
            return res

        return wrapper
    return decorator


@tags("p")
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))


import unittest

class TagsTests(unittest.TestCase):
    def test_zero_second(self):
        @tags('h1')
        def to_upper(text):
            return text.upper()
        self.assertEqual(to_upper('hello'), '<h1>HELLO</h1>')

if __name__ == '__main__':
    unittest.main()