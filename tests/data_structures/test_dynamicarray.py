# pylint: disable=R0904

import unittest
from src.data_structures.dynamicarray import DynamicArray


class TestDynamicArray(unittest.TestCase):
    def test_capacity_default(self) -> None:
        dynamicarray = DynamicArray()
        self.assertEqual(dynamicarray.capacity, 10)

    def test_capacity_non_default(self) -> None:
        dynamicarray = DynamicArray(5)
        self.assertEqual(dynamicarray.capacity, 5)

    def test_contains_true(self) -> None:
        dynamicarray = DynamicArray()
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.add_last(3)
        dynamicarray.add_last(4)
        dynamicarray.add_last(5)
        self.assertTrue(dynamicarray.contains(5))

    def test_contains_false(self) -> None:
        dynamicarray = DynamicArray()
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.add_last(3)
        dynamicarray.add_last(4)
        dynamicarray.add_last(5)
        self.assertFalse(dynamicarray.contains(7))

    def test_contains_on_empty_list(self) -> None:
        dynamicarray = DynamicArray()
        self.assertFalse(dynamicarray.contains(1))

    def test_get_single_add(self) -> None:
        dynamicarray = DynamicArray()
        dynamicarray.add_last(1)
        self.assertEqual(dynamicarray.get(0), 1)

    def test_get_multiple_adds(self) -> None:
        dynamicarray = DynamicArray()
        for i in range(10):
            dynamicarray.add_last(i)
        self.assertEqual(dynamicarray.get(9), 9)

    def test_get_single_removal(self) -> None:
        dynamicarray = DynamicArray()
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.remove_last()
        self.assertEqual(dynamicarray.get(0), 1)

    def test_get_multiple_removals(self) -> None:
        dynamicarray = DynamicArray()
        for i in range(10):
            dynamicarray.add_last(i)

        dynamicarray.remove_last()
        dynamicarray.remove(0)
        self.assertEqual(dynamicarray.get(7), 8)

    def test_get_empty_array(self) -> None:
        dynamicarray = DynamicArray()
        with self.assertRaises(IndexError) as err:
            dynamicarray.get(0)
        self.assertEqual("Array index is out of range", str(err.exception))

    def test_get_empty_invalid_index(self) -> None:
        dynamicarray = DynamicArray()
        dynamicarray.add_last(1)
        with self.assertRaises(IndexError) as err:
            dynamicarray.get(1)
        self.assertEqual("Array index is out of range", str(err.exception))

    def test_add_single_add(self) -> None:
        dynamicarray = DynamicArray(3)
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.add_last(3)
        self.assertEqual(str(dynamicarray), "[1, 2, 3]")

        dynamicarray.add(1, 9)
        self.assertEqual(str(dynamicarray), "[1, 9, 2, 3]")

    def test_add_multiple_adds(self) -> None:
        dynamicarray = DynamicArray(3)
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.add_last(3)
        self.assertEqual(str(dynamicarray), "[1, 2, 3]")

        dynamicarray.add(1, 9)
        dynamicarray.add(1, 8)
        self.assertEqual(str(dynamicarray), "[1, 8, 9, 2, 3]")

    def test_add_invalid_index(self) -> None:
        dynamicarray = DynamicArray()
        with self.assertRaises(IndexError) as error:
            dynamicarray.add(11, 1)
        self.assertEqual("Array index is out of range", str(error.exception))

    def test_add_last_single_add(self) -> None:
        dynamicarray = DynamicArray()
        dynamicarray.add_last(1)
        self.assertEqual(str(dynamicarray), "[1]")

    def test_add_last_multiple_adds(self) -> None:
        dynamicarray = DynamicArray()
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.add_last(3)
        self.assertEqual(str(dynamicarray), "[1, 2, 3]")

    def test_remove_single_remove(self) -> None:
        dynamicarray = DynamicArray(3)
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.add_last(3)
        self.assertEqual(str(dynamicarray), "[1, 2, 3]")

        removed_elem = dynamicarray.remove(1)
        self.assertEqual(str(dynamicarray), "[1, 3]")
        self.assertEqual(removed_elem, 2)

    def test_remove_multiple_removes(self) -> None:
        dynamicarray = DynamicArray(3)
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.add_last(3)
        self.assertEqual(str(dynamicarray), "[1, 2, 3]")

        dynamicarray.remove(1)
        removed_elem = dynamicarray.remove(1)
        self.assertEqual(str(dynamicarray), "[1]")
        self.assertEqual(removed_elem, 3)

    def test_remove_invalid_index(self) -> None:
        dynamicarray = DynamicArray()
        with self.assertRaises(IndexError) as error:
            dynamicarray.remove(1)
        self.assertEqual("Array index is out of range", str(error.exception))

    def test_remove_last_single_remove(self) -> None:
        dynamicarray = DynamicArray(3)
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.add_last(3)
        self.assertEqual(str(dynamicarray), "[1, 2, 3]")

        elem = dynamicarray.remove_last()
        self.assertEqual(elem, 3)
        self.assertEqual(str(dynamicarray), "[1, 2]")

    def test_remove_last_multiple_removes(self) -> None:
        dynamicarray = DynamicArray(3)
        dynamicarray.add_last(1)
        dynamicarray.add_last(2)
        dynamicarray.add_last(3)
        self.assertEqual(str(dynamicarray), "[1, 2, 3]")

        elem = dynamicarray.remove_last()
        self.assertEqual(elem, 3)
        self.assertEqual(str(dynamicarray), "[1, 2]")

    def test_remove_last_empty_array(self) -> None:
        dynamicarray = DynamicArray(3)
        with self.assertRaises(IndexError) as err:
            dynamicarray.remove_last()
        self.assertEqual("Array is empty", str(err.exception))

    def test_resize(self) -> None:
        dynamicarray = DynamicArray()
        for i in range(11):
            dynamicarray.add_last(i)
        self.assertEqual(dynamicarray.capacity, 20)

    def test_size_default(self) -> None:
        dynamicarray = DynamicArray()
        self.assertEqual(dynamicarray.size, 0)

    def test_size_single_add_last(self) -> None:
        dynamicarray = DynamicArray()
        dynamicarray.add_last(1)
        self.assertEqual(dynamicarray.size, 1)

    def test_size_multiple_add_lasts(self) -> None:
        dynamicarray = DynamicArray()
        for i in range(10):
            dynamicarray.add_last(i)
        self.assertEqual(dynamicarray.size, 10)

    def test_size_single_remove_last(self) -> None:
        dynamicarray = DynamicArray()
        for i in range(10):
            dynamicarray.add_last(i)

        dynamicarray.remove_last()
        self.assertEqual(dynamicarray.size, 9)

    def test_size_multiple_remove_lasts(self) -> None:
        dynamicarray = DynamicArray()
        for i in range(10):
            dynamicarray.add_last(i)

        dynamicarray.remove_last()
        dynamicarray.remove_last()
        self.assertEqual(dynamicarray.size, 8)
