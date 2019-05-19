import json

from placeInfo import PlaceInfo
from place import Place


class ResortsInfo(PlaceInfo):
    """ADT for interaction with resorts data"""
    def create(self, path, key):
        """
        Create ADT with resorts data

        :param path: path of file with cities data
        :param key: cultural resort, ski resort...
        :return: None
        """
        with open(path, encoding='utf-8') as f:
            resorts = json.load(f)[key]
        i = 0
        for resort in resorts.items():
            self[i] = Place(name=resort[0],
                            extra_data={"picture": resort[1]})
            i += 1
