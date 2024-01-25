import unittest
from src.data_structures.queue import Queue


class TestQueue(unittest.TestCase):

    def test_add_single_item(self) -> None:
        queue: Queue[int] = Queue()
        queue.enqueue(5)
        self.assertEqual(5, queue.peek())

    def test_add_multiple_items(self) -> None:
        queue: Queue[bool] = Queue()
        queue.enqueue(True)
        queue.enqueue(False)
        queue.enqueue(True)
        self.assertEqual(True, queue.peek())

    def test_add_after_remove(self) -> None:
        queue: Queue[int] = Queue()
        queue.enqueue(5)
        queue.dequeue()
        queue.enqueue(63)
        self.assertEqual(63, queue.peek())

    def test_remove_after_single_add(self) -> None:
        queue: Queue[int] = Queue()
        queue.enqueue(5)
        removed = queue.dequeue()
        self.assertEqual(5, removed)

    def test_remove_after_multiple_adds(self) -> None:
        queue: Queue[float] = Queue()
        queue.enqueue(5.9)
        queue.enqueue(8.214)
        queue.enqueue(3.77)
        removed = queue.dequeue()
        self.assertEqual(5.9, removed)

    def test_multiple_removes_after_multiple_adds(self) -> None:
        queue: Queue[float] = Queue()
        queue.enqueue(5.9)
        queue.enqueue(8.214)
        queue.enqueue(3.77)
        queue.dequeue()
        removed = queue.dequeue()
        self.assertEqual(8.214, removed)

    def test_remove_on_empty_queue_raises_exception(self) -> None:
        queue: Queue[int] = Queue()
        with self.assertRaises(Exception):
            queue.dequeue()

    def test_peek_after_single_add(self) -> None:
        queue: Queue[int] = Queue()
        queue.enqueue(5)
        self.assertEqual(5, queue.peek())

    def test_peek_after_multiple_adds(self) -> None:
        queue: Queue[str] = Queue()
        queue.enqueue('first item')
        queue.enqueue('second item')
        queue.enqueue('third item')
        self.assertEqual('first item', queue.peek())

    def test_peek_after_add_remove(self) -> None:
        queue: Queue[str] = Queue()
        queue.enqueue('first item')
        queue.enqueue('second item')
        queue.enqueue('third item')
        queue.dequeue()
        self.assertEqual('second item', queue.peek())

    def test_empty_on_new_queue_is_true(self) -> None:
        queue: Queue[int] = Queue()
        self.assertTrue(queue.isEmpty())

    def test_empty_after_add_is_false(self) -> None:
        queue: Queue[int] = Queue()
        queue.enqueue(5)
        self.assertFalse(queue.isEmpty())

    def test_empty_after_remove_is_true(self) -> None:
        queue: Queue[int] = Queue()
        queue.enqueue(5)
        queue.dequeue()
        self.assertTrue(queue.isEmpty())

    def test_peek_on_empty_queue_raises_exception(self) -> None:
        queue: Queue[int] = Queue()
        with self.assertRaises(Exception):
            queue.peek()


if __name__ == '__main__':
    unittest.main()
