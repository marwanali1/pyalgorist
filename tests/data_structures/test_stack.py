import unittest
from src.data_structures.stack import Stack


class TestStack(unittest.TestCase):

    def test_push_single_item(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(5)
        self.assertEqual(5, stack.peek())

    def test_push_multiple_items(self) -> None:
        stack: Stack[bool] = Stack()
        stack.push(True)
        stack.push(False)
        stack.push(True)
        self.assertEqual(True, stack.peek())

    def test_push_after_pop(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(5)
        stack.pop()
        stack.push(63)
        self.assertEqual(63, stack.peek())

    def test_pop_after_single_push(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(5)
        popped = stack.pop()
        self.assertEqual(5, popped)

    def test_pop_after_multiple_pushes(self) -> None:
        stack: Stack[float] = Stack()
        stack.push(5.9)
        stack.push(8.214)
        stack.push(3.77)
        popped = stack.pop()
        self.assertEqual(3.77, popped)

    def test_multiple_pops_after_multiple_pushes(self) -> None:
        stack: Stack[float] = Stack()
        stack.push(5.9)
        stack.push(8.214)
        stack.push(3.77)
        stack.pop()
        popped = stack.pop()
        self.assertEqual(8.214, popped)

    def test_pop_on_empty_stack_raises_exception(self) -> None:
        stack: Stack[int] = Stack()
        with self.assertRaises(Exception):
            stack.pop()

    def test_peek_after_single_push(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(5)
        self.assertEqual(5, stack.peek())

    def test_peek_after_multiple_pushes(self) -> None:
        stack: Stack[str] = Stack()
        stack.push('first item')
        stack.push('second item')
        stack.push('third item')
        self.assertEqual('third item', stack.peek())

    def test_peek_after_push_pop(self) -> None:
        stack: Stack[str] = Stack()
        stack.push('first item')
        stack.push('second item')
        stack.push('third item')
        stack.pop()
        self.assertEqual('second item', stack.peek())

    def test_empty_on_new_stack_is_true(self) -> None:
        stack: Stack[int] = Stack()
        self.assertTrue(stack.isEmpty())

    def test_empty_after_push_is_false(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(5)
        self.assertFalse(stack.isEmpty())

    def test_empty_after_pop_is_true(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(5)
        stack.pop()
        self.assertTrue(stack.isEmpty())

    def test_peek_on_empty_stack_raises_exception(self) -> None:
        stack: Stack[int] = Stack()
        with self.assertRaises(Exception):
            stack.peek()


if __name__ == '__main__':
    unittest.main()
