import unittest
from src.algorithms.sort.quicksort import QuicksortArray


class TestQuicksort(unittest.TestCase):
    def test_character_sort(self):
        actual = QuicksortArray(
            ["I", "N", "S", "E", "R", "T", "I", "O", "N", "S", "O", "R", "T"]
        )
        actual.quicksort(0, len(actual) - 1)

        expected = ["E", "I", "I", "N", "N", "O", "O", "R", "R", "S", "S", "T", "T"]
        self.assertEqual(actual.elems, expected)

    def test_string_sort(self):
        actual = QuicksortArray(["MIKE", "BOB", "SALLY", "JILL", "JAN"])
        actual.quicksort(0, len(actual) - 1)

        expected = ["BOB", "JAN", "JILL", "MIKE", "SALLY"]
        self.assertEqual(actual.elems, expected)

    def test_integer_sort(self):
        actual = QuicksortArray([154, 245, 568, 324, 654, 324])
        actual.quicksort(0, len(actual) - 1)

        expected = [154, 245, 324, 324, 568, 654]
        self.assertEqual(actual.elems, expected)


if __name__ == "__main__":
    unittest.main()
