import unittest
from src.data_structures.linkedlist import LinkedList


class TestStack(unittest.TestCase):
    def test_contains_true(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        linkedlist.add_last(4)
        linkedlist.add_last(5)
        self.assertTrue(linkedlist.contains(5))

    def test_contains_false(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        linkedlist.add_last(4)
        linkedlist.add_last(5)
        self.assertFalse(linkedlist.contains(7))
    
    def test_contains_on_empty_list(self) -> None:
        linkedlist = LinkedList()
        self.assertFalse(linkedlist.contains(1))

    def test_get(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        self.assertEqual(linkedlist.get(0), 1)

    def test_get_index_out_of_range(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        with self.assertRaises(IndexError) as err:
            linkedlist.get(-1)
        self.assertEqual("List index is out of range", str(err.exception))

    def test_get_on_empty_list(self) -> None:
        linkedlist = LinkedList()
        with self.assertRaises(IndexError) as err:
            linkedlist.get(0)
        self.assertEqual("List index is out of range", str(err.exception))

    def test_add_single_add(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

        linkedlist.add(2, 4)
        self.assertEqual(str(linkedlist), "[1, 2, 4, 3]")

    def test_add_multiple_adds(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

        linkedlist.add(1, 4)
        linkedlist.add(1, 5)
        self.assertEqual(str(linkedlist), "[1, 5, 4, 2, 3]")

    def test_add_add_at_start(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

        linkedlist.add(0, 4)
        self.assertEqual(str(linkedlist), "[4, 1, 2, 3]")

    def test_add_add_at_end(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

        linkedlist.add(3, 4)
        self.assertEqual(str(linkedlist), "[1, 2, 3, 4]")

    def test_add_index_out_of_range(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        with self.assertRaises(IndexError) as err:
            linkedlist.add(-1, 3)
        self.assertEqual("List index is out of range", str(err.exception))

    def test_add_first_single_add(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_first(1)
        self.assertEqual(str(linkedlist), "[1]")

    def test_add_first_multiple_adds(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_first(1)
        linkedlist.add_first(2)
        linkedlist.add_first(3)
        self.assertEqual(str(linkedlist), "[3, 2, 1]")

    def test_add_last_single_add(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        self.assertEqual(str(linkedlist), "[1]")

    def test_add_last_multiple_adds(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

    def test_remove_single_remove(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

        removed_data = linkedlist.remove(1)
        self.assertEqual(str(linkedlist), "[1, 3]")
        self.assertEqual(removed_data, 2)

    def test_remove_multiple_removes(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

        linkedlist.remove(1)
        removed_data = linkedlist.remove(1)
        self.assertEqual(str(linkedlist), "[1]")
        self.assertEqual(removed_data, 3)

    def test_remove_remove_at_start(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

        removed_data = linkedlist.remove(0)
        self.assertEqual(str(linkedlist), "[2, 3]")
        self.assertEqual(removed_data, 1)

    def test_remove_remove_at_end(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

        removed_data = linkedlist.remove(2)
        self.assertEqual(str(linkedlist), "[1, 2]")
        self.assertEqual(removed_data, 3)

    def test_remove_invalid_index(self) -> None:
        linkedlist = LinkedList()
        with self.assertRaises(IndexError) as error:
            linkedlist.remove(1)
        self.assertEqual("List index is out of range", str(error.exception))

    def test_remove_first_single_remove(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        self.assertEqual(linkedlist.remove_first(), 1)

    def test_remove_first_multiple_removes(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        linkedlist.add_last(4)
        linkedlist.add_last(5)
        linkedlist.remove_first()
        self.assertEqual(linkedlist.remove_first(), 2)

    def test_remove_first_on_empty_list(self) -> None:
        linkedlist = LinkedList()
        with self.assertRaises(IndexError) as err:
            linkedlist.remove_first()
        self.assertEqual("List is empty", str(err.exception))

    def test_remove_last_single_remove(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        self.assertEqual(linkedlist.remove_last(), 2)

    def test_remove_last_multiple_removes(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        linkedlist.add_last(4)
        linkedlist.add_last(5)
        linkedlist.remove_last()
        self.assertEqual(linkedlist.remove_last(), 4)

    def test_remove_last_on_empty_list(self) -> None:
        linkedlist = LinkedList()
        with self.assertRaises(IndexError) as err:
            linkedlist.remove_last()
        self.assertEqual("List is empty", str(err.exception))

    def test_reverse_single_node(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        self.assertEqual(str(linkedlist), "[1]")

        linkedlist.reverse()
        self.assertEqual(str(linkedlist), "[1]")

    def test_reverse_multiple_nodes(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

        linkedlist.reverse()
        self.assertEqual(str(linkedlist), "[3, 2, 1]")

    def test_reverse_double_reverse(self) -> None:
        linkedlist = LinkedList()
        linkedlist.add_last(1)
        linkedlist.add_last(2)
        linkedlist.add_last(3)

        linkedlist.reverse()
        self.assertEqual(str(linkedlist), "[3, 2, 1]")

        linkedlist.reverse()
        self.assertEqual(str(linkedlist), "[1, 2, 3]")

    def test_reverse_on_empty_list(self) -> None:
        linkedlist = LinkedList()
        self.assertEqual(str(linkedlist), "[]")


if __name__ == "__main__":
    unittest.main()
