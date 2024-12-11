import unittest
from src.algorithms.sort.heapsort import heapsort, max_heapsort


class TestQuicksort(unittest.TestCase):
    def test_character_sort(self):
        given = ["I", "N", "S", "E", "R", "T", "I", "O", "N", "S", "O", "R", "T"]
        expected = ["E", "I", "I", "N", "N", "O", "O", "R", "R", "S", "S", "T", "T"]
        self.assertEqual(heapsort(given), expected)

    def test_string_sort(self):
        given = ["MIKE", "BOB", "SALLY", "JILL", "JAN"]
        expected = ["BOB", "JAN", "JILL", "MIKE", "SALLY"]
        self.assertEqual(heapsort(given), expected)

    def test_integer_sort(self):
        given = [154, 245, 568, 324, 654, 324]
        expected = [154, 245, 324, 324, 568, 654]
        self.assertEqual(heapsort(given), expected)

    def test_character_sort_maxheap(self):
        given = ["I", "N", "S", "E", "R", "T", "I", "O", "N", "S", "O", "R", "T"]
        expected = ["T", "T", "S", "S", "R", "R", "O", "O", "N", "N", "I", "I", "E"]
        self.assertEqual(max_heapsort(given), expected)

    def test_string_sort_maxheap(self):
        given = ["MIKE", "BOB", "SALLY", "JILL", "JAN"]
        expected = ["SALLY", "MIKE", "JILL", "JAN", "BOB"]
        self.assertEqual(max_heapsort(given), expected)

    def test_integer_sort_maxheap(self):
        given = [154, 245, 568, 324, 654, 324]
        expected = [654, 568, 324, 324, 245, 154]
        self.assertEqual(max_heapsort(given), expected)


if __name__ == "__main__":
    unittest.main()
