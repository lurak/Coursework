import os

from SimpleSite.constData import CULTURAL_RESORTS, SKI_RESORTS, SEA_RESORTS


def write_wiki(path, place):
    """
    Create file with wiki information about place
    :param path: str
    :param place:Place
    :return:
    """
    with open(path, 'w', encoding='utf-8') as f:
        place.wiki_information()
        f.write(place.extra_data["wiki information"].replace('===', '\n').replace('==', '\n'))


if __name__ == "__main__":
    for place in SEA_RESORTS:
        try:
            write_wiki(os.path.abspath("cities_wiki\\{}.txt".format(place.name)), place)
        except:
            pass

    for place in CULTURAL_RESORTS:
        try:
            write_wiki(os.path.abspath("cities_wiki\\{}.txt".format(place.name)), place)
        except:
            pass

    for place in SKI_RESORTS:
        try:
            write_wiki(os.path.abspath("cities_wiki\\{}.txt".format(place.name)), place)
        except:
            pass
