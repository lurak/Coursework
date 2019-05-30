import json

from ADT.placeInfo import PlaceInfo
from extra_modules.place import Place


class CityInfo(PlaceInfo):
    """ADT for interaction with resorts data"""
    def create(self, path):
        """
        Create ADT with resorts data

        :param path: path of file with cities data

        :return: None
        """
        i = 0
        with open(path, encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                self.countries[i] = line[:-1]
                i += 1
