from ADT.placeInfo import PlaceInfo
from extra_modules.place import Place


class CityInfo(PlaceInfo):
    """Class for interaction among cities data"""
    def create(self, path):
        """

        Create ADT with cities data

        :param path: path of file with cities data
        :return: None
        """
        with open(path, encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.split(', ')
            self[i] = Place(id=line[0][line[0].index('.')+1:], name=line[1],
                            extra_data={"country": line[2], "country_name": line[3]},
                            latitude=line[4], longitude=line[5][:-1])