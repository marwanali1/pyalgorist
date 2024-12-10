import unittest
from src.algorithms.sort.quicksort import QuicksortArray


class TestQuicksort(unittest.TestCase):
    def test_character_sort(self):
        given = QuicksortArray(["I", "N", "S", "E", "R", "T", "I", "O", "N", "S", "O", "R", "T"])
        given.quicksort(0, len(given) - 1)

        expected = ["E", "I", "I", "N", "N", "O", "O", "R", "R", "S", "S", "T", "T"]
        self.assertEqual(given.array, expected)

    def test_string_sort(self):
        given = QuicksortArray(["MIKE", "BOB", "SALLY", "JILL", "JAN"])
        given.quicksort(0, len(given) - 1)

        expected = ["BOB", "JAN", "JILL", "MIKE", "SALLY"]
        self.assertEqual(given.array, expected)

    def test_integer_sort(self):
        given = QuicksortArray([154, 245, 568, 324, 654, 324])
        given.quicksort(0, len(given) - 1)

        expected = [154, 245, 324, 324, 568, 654]
        self.assertEqual(given.array, expected)


if __name__ == "__main__":
    unittest.main()
