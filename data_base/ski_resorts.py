import requests
import re
from py_translator import Translator


def ski_resorts():
    """
    (None) -> dict

    Return the dictionary of the best ski resorts from site:
    https://tripmydream.ua/blog/podborki/top-6-kraschih-girskolizhnih-kyrortiv-avstrigi
    """
    dictionary = dict()
    resorts = list()
    cities = list()
    site = requests.get("https://travelyourway.com.ua/ua/blog/luchshie-gornolyzhnye-kurorty-evropy/")
    prev_resorts = re.findall('\d?\d\..+</h3>\n', site.text)
    prev_cities = re.findall('Розташування.+\n', site.text)
    for inf in range(len(prev_resorts)):
        resort = re.findall('\w+-?\w+\s', prev_resorts[inf])
        resort = resort[0]
        delete = list(resort)
        delete.remove(' ')
        resort = ''.join(delete)
        if resort == 'Пояна':
            resort += ' Брашов'
        resorts.append(resort)
    for info in range(len(prev_cities)):
         city = re.findall("\w+-?\w+-?\w+\.", prev_cities[info])
         city = city[0]
         delete = list(city)
         delete.remove('.')
         city = ''.join(delete)
         if city == "Кракова":
             city = "Краків"
         cities.append(city)
    for word in range(len(cities)):
        letters = list(cities[word])
        if letters[-1] == 'ї':
            letters[-1] = "я"
        elif letters[-1] == "и":
            letters[-1] = 'а'
        elif letters[-2] == 'л' or letters[-2] == "с":
            continue
        elif letters[-1] == "а":
            letters.pop()
        cities[word] = ''.join(letters)
    for item in range(len(resorts)):
        value = Translator().translate(text=resorts[item], dest='en').text
        dictionary[value] = value
    return dictionary


def austria_resorts():
    """
    (None) -> dict

    Return the dictionary of the best Austrian ski resorts from site:
    https://tripmydream.ua/blog/podborki/top-6-kraschih-girskolizhnih-kyrortiv-avstrigi
    """
    dictionary = dict()
    site = requests.get("https://tripmydream.ua/blog/podborki/top-6-kraschih-girskolizhnih-kyrortiv-avstrigi")
    resorts = re.findall('<h2 >(.+)</h2>', site.text)
    big_city = re.findall('Інсбрук', site.text)
    while len(big_city) != 5:
        big_city.remove('Інсбрук')
    for item in range(len(resorts)):
        value = Translator().translate(text=resorts[item], dest='en').text
        city = Translator().translate(text=big_city[item], dest='en').text
        dictionary[value] = city
    return dictionary


def dict_conecter_ski(dict_1, dict_2):
    """
    (dict, dict) -> dict

    Return one huge dictionary with ski resorts taken from sites:
    https://tripmydream.ua/blog/podborki/top-6-kraschih-girskolizhnih-kyrortiv-avstrigi
    https://travelyourway.com.ua/ua/blog/luchshie-gornolyzhnye-kurorty-evropy/
    """
    keys = [key for key in dict_1]
    values = [value for value in dict_1]
    for item in range(len(keys)):
        dict_2[keys[item]] = values[item]
    return dict_2
