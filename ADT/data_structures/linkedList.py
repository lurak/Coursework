from ADT.data_structures.node import Node
import gc

# A class implementing Multiset as a linked list.


class LinkedList:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None
        self._size = 0

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head is None

    def remove_all(self):
        """
        Remove all elements in multiset
        :return: None
        """
        self._head = None
        gc.collect()
        self._size = 0

    def __len__(self):
        """
        Return number of elements in multiset

        :return: int
        """
        return self._size

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest
        self._size += 1

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next
            self._size -= 1

    def __str__(self):
        """

        :return: data in structure
        """
        result = ""
        node = self._head
        while node is not None:
            result += str(node.item) + '->'
            node = node.next
        return result[:-2]
