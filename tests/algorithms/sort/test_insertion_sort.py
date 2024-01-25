import unittest
from src.algorithms.sort.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_character_sort(self):
        given = ["I", "N", "S", "E", "R", "T", "I", "O", "N", "S", "O", "R", "T"]
        expected = ["E", "I", "I", "N", "N", "O", "O", "R", "R", "S", "S", "T", "T"]
        self.assertEqual(insertion_sort(given), expected)

    def test_string_sort(self):
        given = ["MIKE", "BOB", "SALLY", "JILL", "JAN"]
        expected = ["BOB", "JAN", "JILL", "MIKE", "SALLY"]
        self.assertEqual(insertion_sort(given), expected)

    def test_integer_sort(self):
        given = [154, 245, 568, 324, 654, 324]
        expected = [154, 245, 324, 324, 568, 654]
        self.assertEqual(insertion_sort(given), expected)


if __name__ == "__main__":
    unittest.main()
