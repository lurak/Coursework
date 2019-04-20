import ctypes

# Implements the Array ADT using array capabilities of the ctypes module.


class Array:
    def __init__(self, size):
        """
        Creates an array with size elements.

        :param size: size of array
        """
        if size <= 0:
            raise ValueError("Array size must be > 0")
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """
        Returns the size of the array.
        :return: size of array
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the contents of the index element.

        :param index: index of element to return
        :return: element of array
        """
        if not 0 <= index < len(self):
            raise IndexError("Array subscript out of range")
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.

        :param index: index of place
        :param value: value to put
        :return: None
        """
        if not 0 <= index < len(self):
            raise IndexError("Array subscript out of range")
        self._elements[index] = value

    def clear(self, value):
        """

        Clears the array by setting each element to the given value.

        :param value: value to replace
        :return: None
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """

        Returns the array's iterator for traversing the elements.

        :return: Array Iterator
        """
        return _ArrayIterator(self._elements)


# An iterator for the Array ADT.
class _ArrayIterator:
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[ self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration
