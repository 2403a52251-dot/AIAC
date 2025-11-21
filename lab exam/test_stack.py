"""Unit tests for the Stack class implemented in `stack.py`.

Run with: python -m unittest test_stack.py
"""
import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_push_pop(self):
        print("Starting: test_push_pop")
        s = Stack[int]()
        s.push(1)
        s.push(2)
        self.assertFalse(s.is_empty())
        self.assertEqual(len(s), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.is_empty())

    def test_peek(self):
        print("Starting: test_peek")
        s = Stack[str]()
        s.push('a')
        self.assertEqual(s.peek(), 'a')
        # peek should not remove the item
        self.assertEqual(len(s), 1)
        self.assertEqual(s.pop(), 'a')

    def test_pop_empty_raises(self):
        print("Starting: test_pop_empty_raises")
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_peek_empty_raises(self):
        print("Starting: test_peek_empty_raises")
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()


if __name__ == '__main__':
    # When run directly, print a short header and run with verbosity so
    # each test name and the print statements are shown in the terminal.
    print("Running test_stack.py")
    unittest.main(verbosity=2)
