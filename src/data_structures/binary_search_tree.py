from typing import TypeVar

T = TypeVar("T")


class TreeNode:
    def __init__(self, value: T = None) -> None:
        self.__value: T = value
        self.__left: TreeNode = None
        self.__right: TreeNode = None

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
            else:
                node.right = __insert(node.right, value)

            return node

        self.__root = __insert(self.root, value)

    def remove(self, value: T) -> T:
        """
        Time Complexity: O(log n)
        """
        pass

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
        pass

    def minimum(self) -> T:
        pass

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