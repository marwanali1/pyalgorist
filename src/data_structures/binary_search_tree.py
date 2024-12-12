from typing import TypeVar
from collections import deque

T = TypeVar("T")


class TreeNode:
    def __init__(self, value: T = None) -> None:
        self._value: T = value
        self._left: TreeNode = None
        self._right: TreeNode = None

    def __repr__(self) -> str:
        rep_str = (
            f"TreeNode(value={self.value}, "
            f"left={self.left is not None}, "
            f"right={self.right is not None})"
        )
        return rep_str

    def __str__(self) -> str:
        pass

    @property
    def left(self) -> T:
        return self._left

    @left.setter
    def left(self, left) -> None:
        self._left = left

    @property
    def right(self) -> T:
        return self._right

    @right.setter
    def right(self, right) -> None:
        self._right = right

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, value: T) -> None:
        self._value = value


class BinarySearchTree:
    def __init__(self, root: TreeNode = None) -> None:
        self._root: TreeNode = root
        self._size: int = 0

    @property
    def root(self) -> TreeNode:
        return self._root

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True

        if not isinstance(other, BinarySearchTree):
            return False

        if len(self) != len(other):
            return False

        def _equal(node_one: TreeNode, node_two: TreeNode) -> bool:
            if not node_one and not node_two:
                return True

            if (not node_one or not node_two) or (node_one.value != node_two.value):
                return False

            same_left = _equal(node_one.left, node_two.left)
            same_right = _equal(node_one.right, node_two.right)
            return same_left and same_right

        return _equal(self.root, other.root)

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    def get_levels(self):
        queue = deque()
        if self.root:
            queue.append(self.root)

        levels = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.value)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return levels

    def insert(self, value: T) -> None:
        """
        Time Complexity: O(log n)
        """

        def _insert(node: TreeNode, value: T) -> TreeNode:
            if not node:
                node = TreeNode(value)
                return node

            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)

            return node

        self._root = _insert(self.root, value)

    def _find_node_to_remove(
        self, node: TreeNode, value: T
    ) -> tuple[TreeNode, TreeNode]:
        curr_node = node
        prev_node = None
        node_to_remove = None

        while curr_node:
            if curr_node.value == value:
                node_to_remove = curr_node
                break

            prev_node = curr_node
            if value < curr_node.left.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return prev_node, node_to_remove

    def _replace_with_successor(self, node: TreeNode) -> TreeNode:
        successor = node.right

        if not successor.left:
            node.value = successor.value
            node.right = successor.right
            return None

        while successor.left:
            parent_of_successor = successor
            successor = successor.left

        if successor.right:
            parent_of_successor.left = successor.right
        else:
            parent_of_successor.left = None

        node.value = successor.value
        return successor

    def remove(self, value: T) -> TreeNode:
        """
        Time Complexity: O(log n)
        """
        prev_node, node_to_remove = self._find_node_to_remove(self.root, value)
        if not node_to_remove:
            return None

        if node_to_remove.left and node_to_remove.right:
            self._replace_with_successor(node_to_remove)
        else:
            node_to_remove_child = node_to_remove.left or node_to_remove.right

            if not prev_node:
                node_to_remove.value = node_to_remove_child.value
                node_to_remove.left = node_to_remove_child.left
                node_to_remove.right = node_to_remove_child.right
            elif node_to_remove == prev_node.left:
                prev_node.left = node_to_remove_child
            elif node_to_remove == prev_node.right:
                prev_node.right = node_to_remove_child

        return node_to_remove

    def search(self, value: T) -> bool:
        """
        Returns true if this tree contains the specified value.
        Time Complexity: O(log n)
        """

        def _search(node: TreeNode, value: T) -> bool:
            if not node:
                return False

            if node.value == value:
                return True

            if value < node.value:
                return _search(node.left, value)

            return _search(node.right, value)

        return _search(self.root, value)

    def maximum(self) -> T:
        def _max(node: TreeNode) -> int:
            if node.right:
                return _max(node.right)

            return node.value

        return _max(self.root)

    def minimum(self) -> T:
        def _min(node: TreeNode) -> int:
            if node.left:
                return _min(node.left)

            return node.value

        return _min(self.root)

    def predecessor(self) -> T:
        pass

    def successor(self) -> T:
        pass

    def inorder(self) -> list[T]:
        """
        Time Complexity: O(n)
        """

        def _inorder(node: TreeNode) -> list[T]:
            if not node:
                return []

            return _inorder(node.left) + [node.value] + _inorder(node.right)

        return _inorder(self.root)

    def preorder(self) -> list:
        """
        Time Complexity: O(n)
        """

        def _preorder(node: TreeNode) -> list[T]:
            if not node:
                return []

            return [node.value] + _preorder(node.left) + _preorder(node.right)

        return _preorder(self.root)

    def postorder(self) -> list[T]:
        """
        Time Complexity: O(n)
        """

        def _postorder(node: TreeNode) -> list[T]:
            if not node:
                return []

            return _postorder(node.left) + _postorder(node.right) + [node.value]

        return _postorder(self.root)
