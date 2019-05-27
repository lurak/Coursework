from arrays import Array


class PlaceInfo:
    """ADT for interaction with places data"""
    def __init__(self, size):
        """

        :param size: size of array
        """
        self.size = size
        self.countries = Array(size)

    def __len__(self):
        """

        :return: int
        """
        return len(self.countries)

    def __setitem__(self, key, value):
        """
        Set item to key position

        :param key: int
        :param value: value
        :return: None
        """
        self.countries.__setitem__(key, value)

    def __getitem__(self, key):
        """
        Return value in key position
        :param key: int
        :return: value
        """
        return self.countries.__getitem__(key)

    def __str__(self):
        """
        View of ADT
        :return: str
        """
        string = ""
        for line in self.countries:
            string += str(line) + '\n'
        return string

