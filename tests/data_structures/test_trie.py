import unittest
from src.data_structures.trie import Trie

class TestTrie(unittest.TestCase):

    def test_add_word_pizza(self) -> None:
        trie = Trie()
        trie.add_word("pizza")
        self.assertTrue(trie.search("pizza"))
    
    def test_add_word_bicycle(self) -> None:
        trie = Trie()
        trie.add_word("bicycle")
        self.assertTrue(trie.search("bicycle"))
    
    def test_search_word_not_found(self) -> None:
        trie = Trie()
        trie.add_word("pizza")
        self.assertFalse(trie.search("pizz"))
    
    def test_starts_with_pi(self) -> None:
        trie = Trie()
        trie.add_word("pizza")
        self.assertTrue(trie.starts_with("pi"))
    
    def test_starts_with_bic(self) -> None:
        trie = Trie()
        trie.add_word("bicycle")
        self.assertTrue(trie.starts_with("bic"))
    
    def test_starts_with_not_found(self) -> None:
        trie = Trie()
        trie.add_word("bicycle")
        self.assertFalse(trie.starts_with("byc"))

if __name__ == '__main__':
    unittest.main()