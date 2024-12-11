# pylint: disable=R0904
# pylint: disable=W0212


import unittest
from src.data_structures.hashtable import HashNode, HashTable


class TestHashNode(unittest.TestCase):
    def test_hashnode_init(self) -> None:
        hashnode = HashNode("test_key", "test_value")
        self.assertEqual(hashnode.key, "test_key")
        self.assertEqual(hashnode.value, "test_value")


class TestHashTable(unittest.TestCase):
    def test_capacity_default(self) -> None:
        hashtable = HashTable()
        self.assertEqual(hashtable.capacity, 16)

    def test_load_factor_default(self) -> None:
        hashtable = HashTable()
        self.assertEqual(hashtable.load_factor, 0.75)

    def test_size_default(self) -> None:
        hashtable = HashTable()
        self.assertEqual(len(hashtable), 0)

    def test_eq_true(self) -> None:
        hashtable_1 = HashTable(from_dict={"one": 1, "two": 2})
        hashtable_2 = HashTable(from_dict={"one": 1, "two": 2})
        self.assertEqual(hashtable_1, hashtable_2)

    def test_eq_false(self) -> None:
        hashtable_1 = HashTable(from_dict={"one": 1})
        hashtable_2 = HashTable(from_dict={"one": 1, "two": 2})
        self.assertNotEqual(hashtable_1, hashtable_2)

    def test_len(self) -> None:
        hashtable = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        self.assertEqual(len(hashtable), 5)

    def test_len_empty_hashtable(self) -> None:
        hashtable = HashTable()
        self.assertEqual(len(hashtable), 0)

    def test_repr(self) -> None:
        hashtable = HashTable(from_dict={"one": 1, "two": 2, "three": 3})
        self.assertEqual(repr(hashtable), f"HashTable({hashtable})")

    def test_str(self) -> None:
        hashtable = HashTable(from_dict={"one": 1, "two": 2, "three": 3})
        self.assertEqual(str(hashtable), "{'one': 1, 'two': 2, 'three': 3}")

    def test_hash_code(self) -> None:
        hashtable = HashTable()
        actual = hashtable._hash_code("one")
        expected = 110182
        self.assertEqual(actual, expected)

    def test_index(self) -> None:
        hashtable = HashTable()
        actual = hashtable._index("one")
        expected = 110182 % hashtable.capacity
        self.assertEqual(actual, expected)

    def test_exceeds_load_factor_false(self) -> None:
        hashtable = HashTable(
            from_dict={
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
                "ten": 10,
                "eleven": 11,
                "twelve": 12,
            },
        )
        self.assertFalse(hashtable._exceeds_load_factor())

    def test_resize(self) -> None:
        actual = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3},
        )
        self.assertEqual(actual.capacity, 16)

        actual._resize()
        self.assertEqual(actual.capacity, 32)

        expected = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3},
        )
        self.assertEqual(actual, expected)

    def test_contains_key_true(self) -> None:
        hashtable = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        self.assertTrue(hashtable.contains_key("two"))

    def test_contains_key_false(self) -> None:
        hashtable = HashTable(from_dict={"one": 1, "two": 2, "four": 4, "five": 5})
        self.assertFalse(hashtable.contains_key("three"))

    def test_contains_value_true(self) -> None:
        hashtable = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        self.assertTrue(hashtable.contains_value(2))

    def test_contains_value_false(self) -> None:
        hashtable = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        self.assertFalse(hashtable.contains_value(7))

    def test_empty_true(self) -> None:
        hashtable = HashTable()
        self.assertTrue(hashtable.empty())

    def test_empty_false(self) -> None:
        hashtable = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        self.assertFalse(hashtable.empty())

    def test_get(self) -> None:
        hashtable = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        self.assertEqual(hashtable.get("three"), 3)

    def test_get_empty_hashtable(self) -> None:
        hashtable = HashTable()
        with self.assertRaises(KeyError):
            hashtable.get("three")

    def test_get_invalid_key(self) -> None:
        hashtable = HashTable(from_dict={"one": 1, "two": 2, "four": 4, "five": 5})
        with self.assertRaises(KeyError):
            hashtable.get("three")

    def test_keys(self) -> None:
        hashtable = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        self.assertEqual(hashtable.keys(), ["five", "four", "one", "two", "three"])

    def test_put_single_put(self) -> None:
        actual = HashTable()
        actual.put("one", 1)

        expected = {"one": 1}
        self.assertEqual(actual, HashTable(from_dict=expected))

    def test_put_multiple_puts(self) -> None:
        actual = HashTable()
        actual.put("three", 3)
        actual.put("five", 5)
        actual.put("one", 1)
        actual.put("four", 4)
        actual.put("two", 2)

        expected = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        self.assertEqual(actual, expected)

    def test_remove_single_remove(self) -> None:
        hashtable = HashTable(from_dict={"one": 1})
        self.assertEqual(hashtable.remove("one"), 1)
        self.assertTrue(hashtable.empty())

    def test_remove_multiple_removes(self) -> None:
        actual = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        actual.remove("two")
        actual.remove("five")

        expected = HashTable(from_dict={"one": 1, "three": 3, "four": 4})
        self.assertEqual(actual, expected)

    def test_remove_invalid_key(self) -> None:
        hashtable = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        with self.assertRaises(KeyError):
            hashtable.get("six")

    def test_remove_empty(self) -> None:
        hashtable = HashTable()
        with self.assertRaises(KeyError):
            hashtable.get("one")

    def test_values(self) -> None:
        hashtable = HashTable(
            from_dict={"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
        )
        self.assertEqual(hashtable.values(), [5, 4, 1, 2, 3])
