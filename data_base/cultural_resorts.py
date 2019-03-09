import requests
import re
from sparta import decode


def few_resorts():
    """
    (None) -> dict

    Return the dictionary of famous and beautiful cities of Europe.
    Data are taken from site:
    https://www.obozrevatel.com/ukr/travel/news/top-10-nejmovirnih-mist-evropi-yaki-potribno-vidvidati.htm
    """
    dictionary = dict()
    site = requests.get(
        "https://www.obozrevatel.com/ukr/travel/news/top-10-nejmovirnih-mist-evropi-yaki-potribno-vidvidati.htm")
    resorts = re.findall('<h2>(\w+),\s\w+</h2>', site.text)
    resorts.remove("Оломоуц")
    for item in range(len(resorts)):
        dictionary[resorts[item]] = decode(resorts[item])
        print(resorts[item])
    return dictionary


def many_resorts():
    """
    (None) -> dict

    Return a huge list of different cities of Europe.
    Data are taken from site:
    https://andy-travelua.livejournal.com/389517.html
    """
    dictionary = dict()
    cite = requests.get("https://andy-travelua.livejournal.com/389517.html")
    resorts = re.findall('\d?\d\.\s([А-Я]+\s?[А-Я]+)\s', cite.text)
    resorts.remove('ЗАМКИ СЛОВАЧЧИНИ')
    resorts.remove("САКСОНСЬКА")
    resorts.remove("СРЕМСКИ КАРЛОВЦИ")
    for word in range(len(resorts)):
        lst = list(resorts[word])
        for letter in range(1, len(lst)):
            lst[letter] = lst[letter].lower()
        resorts[word] = ''.join(lst)
    for item in range(len(resorts)):
        dictionary[resorts[item]] = resorts[item]
    return dictionary

def dict_conecter_cultural(dict_1, dict_2):
    """
    (dict, dict) -> dict

    Return an united dictionary with many famous cities of Europe.
    Data are taken from sites:
    https://andy-travelua.livejournal.com/389517.html
    https://www.obozrevatel.com/ukr/travel/news/top-10-nejmovirnih-mist-evropi-yaki-potribno-vidvidati.htm
    """
    keys = [key for key in dict_1]
    values = [value for value in dict_1]
    for item in range(len(keys)):
        dict_2[keys[item]] = values[item]
    return dict_2
