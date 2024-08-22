import unittest
from src.data_structures.heap import Heap


class TestHeap(unittest.TestCase):
    def test_push_single_push(self) -> None:
        heap = Heap()
        heap.push(1)
        self.assertEqual(str(heap), "[1]")

    def test_push_multiple_pushs(self) -> None:
        heap = Heap()
        heap.push(1)
        heap.push(2)
        heap.push(3)
        heap.push(4)
        heap.push(5)
        self.assertEqual(str(heap), "[5, 4, 2, 1, 3]")

    def test_pop_single_pop(self) -> None:
        heap = Heap()
        heap.push(1)
        heap.push(2)
        heap.push(3)
        heap.push(4)
        heap.push(5)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(str(heap), "[4, 3, 2, 1]")

    def test_pop_multiple_pops(self) -> None:
        heap = Heap()
        heap.push(1)
        heap.push(2)
        heap.push(3)
        heap.push(4)
        heap.push(5)
        heap.pop()
        heap.pop()
        heap.pop()
        heap.pop()
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(str(heap), "[]")

    def test_pop_on_empty_heap(self) -> None:
        heap = Heap()
        with self.assertRaises(IndexError) as err:
            heap.pop()
        self.assertEqual("Heap is empty", str(err.exception))

    def test_peek(self) -> None:
        heap = Heap()
        heap.push(1)
        heap.push(2)
        heap.push(3)
        self.assertEqual(heap.peek(), 3)
        self.assertEqual(str(heap), "[3, 1, 2]")

    def test_peek_on_empty_heap(self) -> None:
        heap = Heap()
        self.assertIsNone(heap.peek())
