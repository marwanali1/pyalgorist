import unittest
from src.data_structures.trie import Trie


class TestTrie(unittest.TestCase):
    def test_add_word_single_add(self) -> None:
        trie = Trie()
        trie.add_word("bike")
        self.assertTrue(trie.contains_word("bike"))

    def test_add_word_multiple_adds(self) -> None:
        trie = Trie()
        trie.add_word("bat")
        trie.add_word("can")
        trie.add_word("cat")
        self.assertTrue(trie.contains_word("can"))

    def test_contains_word_word_not_found(self) -> None:
        trie = Trie()
        trie.add_word("bike")
        self.assertFalse(trie.contains_word("bik"))

    def test_prefix_search_pi(self) -> None:
        trie = Trie()
        trie.add_word("pizza")
        self.assertIsNotNone(trie.prefix_search("pi"))

    def test_prefix_search_bic(self) -> None:
        trie = Trie()
        trie.add_word("bicycle")
        self.assertIsNotNone(trie.prefix_search("bic"))

    def test_prefix_search_not_found(self) -> None:
        trie = Trie()
        trie.add_word("bicycle")
        self.assertIsNotNone(trie.prefix_search("byc"))

    def test_collect_all_words(self) -> None:
        trie = Trie()
        trie.add_word("bat")
        trie.add_word("can")
        trie.add_word("cat")
        self.assertEqual(trie.collect_all_words(), ["bat", "can", "cat"])

    def test_collect_all_words_empty_trie(self) -> None:
        trie = Trie()
        self.assertEqual(trie.collect_all_words(), [])

    def test_autocomplete(self) -> None:
        trie = Trie()
        trie.add_word("bat")
        trie.add_word("can")
        trie.add_word("cat")
        trie.add_word("cart")
        self.assertEqual(trie.auto_complete("ca"), ["n", "t", "rt"])

    def test_autocomplete_no_recommendations(self) -> None:
        trie = Trie()
        trie.add_word("bat")
        trie.add_word("can")
        trie.add_word("cat")
        trie.add_word("cart")
        self.assertEqual(trie.auto_complete("cab"), [])

    def test_autocorrect(self) -> None:
        trie = Trie()
        trie.add_word("cat")
        trie.add_word("catnap")
        trie.add_word("catnip")
        self.assertEqual(trie.auto_correct("catnar"), "catnap")


if __name__ == "__main__":
    unittest.main()
