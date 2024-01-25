import unittest
from src.algorithms.search.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_target_found(self):
        nums = [0, 1, 2, 3, 4, 5]
        self.assertEqual(binary_search(nums, 2), 2)

    def test_binary_search_target_not_found(self):
        nums = [0, 1, 2, 3, 4, 5]
        self.assertEqual(binary_search(nums, 6), -1)


if __name__ == "__main__":
    unittest.main()
