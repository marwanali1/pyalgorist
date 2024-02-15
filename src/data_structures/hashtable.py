from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")


class HashNode:
    def __init__(self, key: K = None, value: V = None, next=None) -> None:
        self.__key = key
        self.__value = value
        self.next = next

    def __repr__(self) -> str:
        return f"HashNode(key={self.key}, value={self.value}, next={self.next})"

    def __str__(self) -> str:
        return f"({self.key}: {self.value})"

    @property
    def key(self) -> K:
        return self.__key

    @property
    def value(self) -> V:
        return self.__value


class HashTable:
    """
    Hashtable implementation of the Map/Dictionary abstract data type.
    """

    def __init__(
        self, capacity: int = 16, load_factor: float = 0.75, from_dict: dict = None
    ) -> None:
        self.__capacity: int = capacity
        self.__load_factor: float = load_factor
        self.__size: int = 0
        self.__buckets: list[HashNode] = [None] * self.__capacity

        if from_dict:
            for key, value in from_dict.items():
                self.put(key, value)

    @property
    def buckets(self) -> list[HashNode]:
        """
        An array of linkedlists that holds key-value pairs.
        """
        return self.__buckets

    @property
    def capacity(self) -> int:
        """
        The number of buckets in the hashtable. Note that the hashtable is open: in the case of a "hash collision", a single bucket stores multiple entries, which must be searched sequentially.
        """
        return self.__capacity

    @property
    def load_factor(self) -> float:
        """
        A measure of how full the hashtable is allowed to get before its capacity is automatically increased.
        """
        return self.__load_factor

    def __eq__(self, other: object) -> bool:
        """
        Compares a given other object with this hashtable for equality. For two hashtables h1 and h2 to be equal, each key-value pair in h1 must be in h2 and vice versa.
        """
        if self is other:
            return True

        if type(self) != type(other):
            return False

        if len(self) != len(other):
            return False

        for key in self.keys():
            if not other.contains_key(key) or self.get(key) != other.get(key):
                return False

        return True

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        return f"HashTable({self})"

    def __str__(self) -> str:
        """
        Returns a string representation of this hashtable, containing the String representation of key-value pair.
        """
        if self.empty():
            return "{}"

        elems = {}
        for i in range(self.capacity):
            entry = self.buckets[i]
            while entry:
                elems[entry.key] = entry.value
                entry = entry.next

        return str(elems)

    def __hash_code(self, key: K) -> int:
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

    def __index(self, key: K, alt_capacity: int = None) -> int:
        capacity = alt_capacity if alt_capacity else self.capacity
        return self.__hash_code(key) % capacity

    def __exceeds_load_factor(self) -> bool:
        cur_load = len(self) / self.capacity
        return cur_load > self.load_factor

    def __resize(self) -> None:
        """`
        Increases the capacity of and internally reorganizes this hashtable, in order to accommodate and access its entries more efficiently.
        This method is called automatically when the number of keys in the hashtable exceeds this hashtable's capacity and load factor.
        """
        new_capacity = self.capacity * 2
        new_buckets = [None] * new_capacity
        for i in range(self.capacity):
            entry = self.buckets[i]
            while entry:
                index = self.__index(entry.key, new_capacity)
                new_entry = HashNode(entry.key, entry.value)
                new_entry.next = new_buckets[index]
                new_buckets[index] = new_entry
                entry = entry.next

        self.__capacity = new_capacity
        self.__buckets = new_buckets

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
        return not len(self)

    def get(self, key: K) -> V:
        """
        Returns the value to which the specified key is mapped, or null if this map contains no mapping for the key.
        Time complexity: O(n)
        """
        index = self.__index(key)
        entry = self.buckets[index]
        if not entry:
            raise KeyError(key)

        while entry and entry.key != key:
            entry = entry.next

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
                entry = entry.next

        return keys

    def put(self, key: K, value: V) -> None:
        """
        Maps the specified key to the specified value in this hashtable.
        Time complexity: O(1)
        """
        index = self.__index(key)
        new_entry = HashNode(key, value)
        new_entry.next = self.buckets[index]
        self.buckets[index] = new_entry
        self.__size += 1

        if self.__exceeds_load_factor():
            self.__resize()

    def remove(self, key: K) -> V:
        """
        Removes the key (and its corresponding value) from this hashtable.
        Time complexity: O(n)
        """
        index = self.__index(key)
        entry = self.buckets[index]
        if not entry:
            raise KeyError(key)

        head = curr = HashNode(next=entry)
        while curr.next and curr.next.key != key:
            curr = curr.next

        if curr.next.key != key:
            raise KeyError(key)

        value = curr.next.value
        curr.next = curr.next.next
        self.buckets[index] = head.next
        self.__size -= 1
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
                entry = entry.next

        return values
