import os

from SimpleSite.constData import PLACES
import jellyfish
import json
from extra_modules.place import Place


def extra_data(in_path, out_path):
    with open(in_path, encoding='utf-8') as f:
        data = json.loads(f.read())

    for resorts in data:
        for value in data[resorts]:
            longitude = None
            latitude = None
            id = None
            for place in PLACES:
                place = place.split(', ')

                if jellyfish.levenshtein_distance(place[1], value) <= 2:

                    id = place[0]

                    latitude = place[5]
                    longitude = place[4]
            pl = Place(value)
            if id is None:
                try:
                    pl.get_coordinates()
                except:
                    pass
            pl.wiki_information()
            dct = {"picture": data[resorts][value], "id": id,
                   "latitude": latitude, "longitude": longitude,
                   }
            data[resorts][value] = dct
    with open(out_path, 'w', encoding='utf-8') as f2:
        json.dump(data, f2, indent=4)


if __name__ == "__main__":
    extra_data(os.path.abspath("data_base\\data.json"), os.path.abspath("SimpleSite\\files\\resorts.json"))