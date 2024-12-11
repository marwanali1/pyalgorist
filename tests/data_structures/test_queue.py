# pylint: disable=R0904

import unittest
from src.data_structures.queue import Queue


class TestQueue(unittest.TestCase):
    def test_contains_true(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertTrue(5 in queue)

    def test_contains_false(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertFalse(7 in queue)

    def test_contains_on_empty_queue(self) -> None:
        queue = Queue()
        self.assertFalse(1 in queue)

    def test_enqueue_single_enqueue(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(str(queue), "[1]")

    def test_enqueue_multiple_enqueues(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(str(queue), "[1, 2, 3, 4, 5]")

    def test_dequeue_single_dequeue(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(str(queue), "[2, 3, 4, 5]")

    def test_dequeue_multiple_dequeues(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(str(queue), "[]")

    def test_dequeue_on_empty_queue(self) -> None:
        queue = Queue()
        with self.assertRaises(IndexError) as err:
            queue.dequeue()
        self.assertEqual("Queue is empty", str(err.exception))

    def test_peek(self) -> None:
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(str(queue), "[1, 2, 3]")

    def test_peek_on_empty_queue(self) -> None:
        queue = Queue()
        self.assertIsNone(queue.peek())
