import json

from ADT.placeInfo import PlaceInfo
from extra_modules.place import Place


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
                            id=resort[1]["id"],
                            extra_data={"picture": resort[1]["picture"]},
                            latitude=resort[1]["latitude"],
                            longitude=resort[1]["longitude"])
            #self[i].wiki_information()
            i += 1
