import unittest
from src.data_structures.stack import Stack


class TestStack(unittest.TestCase):
    def test_contains_true(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertTrue(stack.contains(5))

    def test_contains_false(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertFalse(stack.contains(7))

    def test_contains_on_empty_stack(self) -> None:
        stack = Stack()
        self.assertFalse(stack.contains(1))

    def test_push_single_push(self) -> None:
        stack = Stack()
        stack.push(1)
        self.assertEqual(str(stack), "[1]")

    def test_push_multiple_pushes(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(str(stack), "[5, 4, 3, 2, 1]")

    def test_pop_single_pop(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(str(stack), "[4, 3, 2, 1]")

    def test_pop_multiple_pops(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(str(stack), "[]")

    def test_pop_on_empty_stack(self) -> None:
        stack = Stack()
        with self.assertRaises(IndexError) as err:
            stack.pop()
        self.assertEqual("Stack is empty", str(err.exception))

    def test_peek(self) -> None:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(str(stack), "[3, 2, 1]")

    def test_peek_on_empty_stack(self) -> None:
        stack = Stack()
        with self.assertRaises(IndexError) as err:
            stack.peek()
        self.assertEqual("Stack is empty", str(err.exception))


if __name__ == "__main__":
    unittest.main()
