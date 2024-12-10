class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


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

    def auto_correct(self, prefix: str) -> TrieNode:
        curr = self.root
        word = ""
        for char in prefix:
            if char not in curr.children:
                return word + self.collect_all_words(curr)[0]
            word += char
            curr = curr.children.get(char)

        return word

    def collect_all_words(self, start_node: TrieNode = None) -> list[str]:

        def __collect_all_words(
            words: list[str], word: str, node: TrieNode
        ) -> list[str]:
            curr = node or self.root
            for key, child in curr.children.items():
                if child.is_end_of_word:
                    words.append(word + key)
                else:
                    __collect_all_words(words, word + key, child)

            return words

        return __collect_all_words([], "", start_node)

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
        def __traverse(node) -> None:
            for key, child in node.children.items():
                print(key)
                if not child.is_end_of_word:
                    __traverse(child)

        __traverse(self.root)
