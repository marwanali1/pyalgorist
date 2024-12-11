from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")


class HashNode:
    def __init__(self, key: K = None, value: V = None, next_node=None) -> None:
        self._key = key
        self._value = value
        self._next_node = next_node

    def __repr__(self) -> str:
        return (
            f"HashNode(key={self.key}, value={self.value}, next_node={self.next_node})"
        )

    def __str__(self) -> str:
        return f"({self.key}: {self.value})"

    @property
    def key(self) -> K:
        return self._key

    @property
    def value(self) -> V:
        return self._value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node


class HashTable:
    """
    Hashtable implementation of the Map/Dictionary abstract data type.
    """

    def __init__(
        self, capacity: int = 16, load_factor: float = 0.75, from_dict: dict = None
    ) -> None:
        self._capacity: int = capacity
        self._load_factor: float = load_factor
        self._size: int = 0
        self._buckets: list[HashNode] = [None] * self._capacity

        if from_dict:
            for key, value in from_dict.items():
                self.put(key, value)

    @property
    def buckets(self) -> list[HashNode]:
        """
        An array of linkedlists that holds key-value pairs.
        """
        return self._buckets

    @property
    def capacity(self) -> int:
        """
        The number of buckets in the hashtable. Note that the hashtable is open: in the case of a
        "hash collision", a single bucket stores multiple entries, which must be searched
        sequentially.
        """
        return self._capacity

    @property
    def load_factor(self) -> float:
        """
        A measure of how full the hashtable is allowed to get before its capacity is automatically
        increased.
        """
        return self._load_factor

    def __eq__(self, other: object) -> bool:
        """
        Compares a given other object with this hashtable for equality. For two hashtables h1 and
        h2 to be equal, each key-value pair in h1 must be in h2 and vice versa.
        """
        if self is other:
            return True

        if not isinstance(other, HashTable):
            return False

        if len(self) != len(other):
            return False

        for key in self.keys():
            if not other.contains_key(key) or self.get(key) != other.get(key):
                return False

        return True

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"HashTable({self})"

    def __str__(self) -> str:
        """
        Returns a string representation of this hashtable, containing the String representation of
        key-value pair.
        """
        if self.empty():
            return "{}"

        elems = {}
        for i in range(self.capacity):
            entry = self.buckets[i]
            while entry:
                elems[entry.key] = entry.value
                entry = entry.next_node

        return str(elems)

    def _hash_code(self, key: K) -> int:
        """
        Returns a hash code value for the given key.
        """
        key_str = str(key)
        key_len = len(key_str)
        hash_code = 0
        for i, char in enumerate(key_str):
            char_hash = ord(char) * pow(31, key_len - (i + 1))
            hash_code += char_hash

        return hash_code

    def _index(self, key: K, alt_capacity: int = None) -> int:
        capacity = alt_capacity if alt_capacity else self.capacity
        return self._hash_code(key) % capacity

    def _exceeds_load_factor(self) -> bool:
        cur_load = len(self) / self.capacity
        return cur_load > self.load_factor

    def _resize(self) -> None:
        """
        Increases the capacity of and internally reorganizes this hashtable, in order to
        accommodate and access its entries more efficiently. This method is called automatically
        when the number of keys in the hashtable exceeds this hashtable's capacity and load factor.
        """
        new_capacity = self.capacity * 2
        new_buckets = [None] * new_capacity
        for i in range(self.capacity):
            entry = self.buckets[i]
            while entry:
                index = self._index(entry.key, new_capacity)
                new_entry = HashNode(entry.key, entry.value)
                new_entry.next_node = new_buckets[index]
                new_buckets[index] = new_entry
                entry = entry.next_node

        self._capacity = new_capacity
        self._buckets = new_buckets

    def contains_key(self, key: K) -> bool:
        """
        Tests if some key maps into the specified value in this hashtable.
        """
        return key in self.keys()

    def contains_value(self, value: V) -> bool:
        """
        Returns true if this hashtable maps one or more keys to this value.
        """
        return value in self.values()

    def empty(self) -> bool:
        """
        Tests if this hashtable maps no keys to values.
        """
        return not self

    def get(self, key: K) -> V:
        """
        Returns the value to which the specified key is mapped, or null if this map contains no
        mapping for the key.
        Time complexity: O(n)
        """
        index = self._index(key)
        entry = self.buckets[index]
        if not entry:
            raise KeyError(key)

        while entry and entry.key != key:
            entry = entry.next_node

        if not entry:
            raise KeyError(key)

        return entry.value

    def keys(self) -> list[K]:
        """
        Returns a list of the keys in this hashtable.
        Time complexity: O(n)
        """
        if self.empty():
            return []

        keys = []
        for i in range(self.capacity):
            entry = self.buckets[i]
            while entry:
                keys.append(entry.key)
                entry = entry.next_node

        return keys

    def put(self, key: K, value: V) -> None:
        """
        Maps the specified key to the specified value in this hashtable.
        Time complexity: O(1)
        """
        index = self._index(key)
        new_entry = HashNode(key, value)
        new_entry.next_node = self.buckets[index]
        self.buckets[index] = new_entry
        self._size += 1

        if self._exceeds_load_factor():
            self._resize()

    def remove(self, key: K) -> V:
        """
        Removes the key (and its corresponding value) from this hashtable.
        Time complexity: O(n)
        """
        index = self._index(key)
        entry = self.buckets[index]
        if not entry:
            raise KeyError(key)

        head = curr = HashNode(next_node=entry)
        while curr.next_node and curr.next_node.key != key:
            curr = curr.next_node

        if curr.next_node.key != key:
            raise KeyError(key)

        value = curr.next_node.value
        curr.next_node = curr.next_node.next_node
        self.buckets[index] = head.next_node
        self._size -= 1
        return value

    def values(self) -> list[V]:
        """
        Returns a list of the values in this hashtable.
        Time complexity: O(n)
        """
        if self.empty():
            return []

        values = []
        for i in range(self.capacity):
            entry = self.buckets[i]
            while entry:
                values.append(entry.value)
                entry = entry.next_node

        return values
