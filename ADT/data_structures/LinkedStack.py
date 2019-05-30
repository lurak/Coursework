from ADT.data_structures.node import Node


class LinkedStack:
    """Data Structure Linked Stack"""
    def __init__(self):

        self._head = None
        self._size = 0

    def __len__(self):
        """

        :return: Stack length
        """
        return self._size

    def push(self, item):
        """
        Add item to Stack
        :param item: some item
        :return:
        """
        self._size += 1
        self._head = Node(item, self._head)

    def peek(self):
        """
        Peek last added element of Stack
        :return: item
        """
        if self.is_empty():
            return None
        return self._head.item

    def pop(self):
        """
        Pop last added elem of STack
        :return: item
        """
        if self.is_empty():
            return None
        self._size -= 1
        item = self.peek()
        self._head = self._head.next
        return item

    def clear(self):
        """
        Clear Stack
        :return:
        """
        self._size = 0
        self._head = None

    def is_empty(self):
        """
        Check if Stack is Empty
        :return:
        """
        return self._head is None
