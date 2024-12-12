from typing import Optional




class TrieNode:
    def __init__(self) -> None:
        self._children: dict[str, TrieNode] = {}
        self._is_end_of_word: bool = False

    @property
    def children(self) -> dict[str, TrieNode]:
        return self._children

    @property
    def is_end_of_word(self) -> bool:
        return self._is_end_of_word

    @is_end_of_word.setter
    def is_end_of_word(self, flag: bool) -> None:
        self._is_end_of_word = flag


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def __str__(self) -> str:
        return str(self.collect_all_words())

    def add_word(self, word: str) -> None:
        """
        Adds a new word to the trie.
        Time Complexity: O(k) where k is the number of characters in the given word
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children.get(char)

        curr.is_end_of_word = True

    def auto_complete(self, prefix: str) -> list[str]:
        curr = self.prefix_search(prefix)

        if not curr:
            return []

        return self.collect_all_words(curr)

    def auto_correct(self, prefix: str) -> str:
        curr = self.root
        word = ""
        for char in prefix:
            if char not in curr.children:
                return word + self.collect_all_words(curr)[0]
            word += char
            curr = curr.children.get(char)

        return word

    def collect_all_words(self, start_node: Optional[TrieNode] = None) -> list[str]:

        def _collect_all_words(
            words: list[str], word: str, node: TrieNode
        ) -> list[str]:
            curr = node or self.root
            for key, child in curr.children.items():
                if child.is_end_of_word:
                    words.append(word + key)
                else:
                    _collect_all_words(words, word + key, child)

            return words

        return _collect_all_words([], "", start_node)

    def contains_word(self, word: str) -> bool:
        """
        Searches the trie for a given word.
        Time Complexity: O(k) where k is the number of characters in the given word
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children.get(char)

        return curr.is_end_of_word

    def prefix_search(self, prefix: str) -> TrieNode:
        """
        Searches the trie for a given prefix.
        Time Complexity: O(k) where k is the number of characters in the given word
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children.get(char)

        return curr

    def traverse(self) -> None:
        def _traverse(node) -> None:
            for key, child in node.children.items():
                print(key)
                if not child.is_end_of_word:
                    _traverse(child)

        _traverse(self.root)
