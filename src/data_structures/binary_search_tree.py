from typing import TypeVar
from collections import deque

T = TypeVar("T")


class TreeNode:
    def __init__(self, value: T = None) -> None:
        self.__value: T = value
        self.__left: TreeNode = None
        self.__right: TreeNode = None

    def __repr__(self) -> str:
        return f"TreeNode(value={self.value}, left={self.left != None}, right={self.right != None})"

    def __str__(self) -> str:
        pass

    @property
    def left(self) -> T:
        return self.__left

    @left.setter
    def left(self, left) -> None:
        self.__left = left

    @property
    def right(self) -> T:
        return self.__right

    @right.setter
    def right(self, right) -> None:
        self.__right = right

    @property
    def value(self) -> T:
        return self.__value

    @value.setter
    def value(self, value: T) -> None:
        self.__value = value


class BinarySearchTree:
    def __init__(self, root: TreeNode = None) -> None:
        self.__root: TreeNode = root
        self.__size: int = 0

    @property
    def root(self) -> TreeNode:
        return self.__root

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True

        if type(self) != type(other):
            return False

        if len(self) != len(other):
            return False

        def __equal(node_one: TreeNode, node_two: TreeNode) -> bool:
            if not node_one and not node_two:
                return True

            if (not node_one or not node_two) or (node_one.value != node_two.value):
                return False

            same_left = __equal(node_one.left, node_two.left)
            same_right = __equal(node_one.right, node_two.right)
            return same_left and same_right

        return __equal(self.root, other.root)

    def __len__(self) -> int:
        return self.__size

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

        def __insert(node: TreeNode, value: T) -> TreeNode:
            if not node:
                node = TreeNode(value)
                return node

            if value < node.value:
                node.left = __insert(node.left, value)
            elif value > node.value:
                node.right = __insert(node.right, value)

            return node

        self.__root = __insert(self.root, value)

    def __find_node_to_remove(
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

    def __replace_with_successor(self, node: TreeNode) -> TreeNode:
        successor = node.right

        if not successor.left:
            node.value = successor.value
            node.right = successor.right
            return

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
        prev_node, node_to_remove = self.__find_node_to_remove(self.root, value)
        if not node_to_remove:
            return None

        if node_to_remove.left and node_to_remove.right:
            self.__replace_with_successor(node_to_remove)
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

        def __search(node: TreeNode, value: T) -> bool:
            if not node:
                return False

            if node.value == value:
                return True

            if value < node.value:
                return __search(node.left, value)
            else:
                return __search(node.right, value)

        return __search(self.root, value)

    def maximum(self) -> T:

        def __max(node: TreeNode) -> int:
            if node.right:
                return __max(node.right)
            else:
                return node.value

        return __max(self.root)

    def minimum(self) -> T:

        def __min(node: TreeNode) -> int:
            if node.left:
                return __min(node.left)
            else:
                return node.value

        return __min(self.root)

    def predecessor(self) -> T:
        pass

    def successor(self) -> T:
        pass

    def inorder(self) -> list[T]:
        """
        Time Complexity: O(n)
        """

        def __inorder(node: TreeNode) -> list[T]:
            if not node:
                return []

            return __inorder(node.left) + [node.value] + __inorder(node.right)

        return __inorder(self.root)

    def preorder(self) -> list:
        """
        Time Complexity: O(n)
        """

        def __preorder(node: TreeNode) -> list[T]:
            if not node:
                return []

            return [node.value] + __preorder(node.left) + __preorder(node.right)

        return __preorder(self.root)

    def postorder(self) -> list[T]:
        """
        Time Complexity: O(n)
        """

        def __postorder(node: TreeNode) -> list[T]:
            if not node:
                return []

            return __postorder(node.left) + __postorder(node.right) + [node.value]

        return __postorder(self.root)
