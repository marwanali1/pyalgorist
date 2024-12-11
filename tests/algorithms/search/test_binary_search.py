import unittest
from src.algorithms.search.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_target_int_found(self):
        nums = [0, 1, 2, 3, 4, 5]
        self.assertEqual(binary_search(nums, 2), 2)

    def test_binary_search_target_int_not_found(self):
        nums = [0, 1, 2, 3, 4, 5]
        self.assertEqual(binary_search(nums, 6), -1)

    def test_binary_search_target_char_found(self):
        chars = ["a", "b", "c", "d", "e", "f"]
        self.assertEqual(binary_search(chars, "d"), 3)

    def test_binary_search_target_char_not_found(self):
        chars = ["a", "b", "c", "d", "e", "f"]
        self.assertEqual(binary_search(chars, "g"), -1)


if __name__ == "__main__":
    unittest.main()
