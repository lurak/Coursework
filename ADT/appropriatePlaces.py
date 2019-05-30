import os

from ADT.data_structures.LinkedStack import LinkedStack
from extra_modules.weather_analysis import Weather
from extra_modules.place import Place


class AppropriatePlaces:
    def __init__(self, cities_ADT, days, init_path=os.path.abspath("SimpleSite\\files\\final_weather.json"),
                                         final_path=os.path.abspath("SimpleSite\\files\\final_weather.json")):
        """

        :param cities_ADT: ResortInfo
        :param days: int
        :param init_path: path where to write down json weather
        :param final_path: path where to write down json weather
        """
        self.init_path = init_path
        self.final_path = final_path
        self.app_cities = LinkedStack()
        self.cities_ADT = cities_ADT
        self.days = days
        try:
            self.create()
        except:
            pass

    def check_city(self, city):
        """

        :param city: Place
        :return: check if place is optimal
        """

        if not isinstance(city, Place):
            raise TypeError("city type should be Place")

        weather = Weather(city.name, self.days, initial_path=self.init_path,
                                                final_path=self.final_path)
        return weather.good_weather()

    def add_city(self, city):
        """
        Add city to ADT

        :param city: Place
        :return: None
        """
        if self.check_city(city):
            self.app_cities.push(city)

    def create(self):
        """
        Fill ADT with optimal cities
        :return: None
        """
        for i in range(len(self.cities_ADT)):
            try:
                with open(os.path.abspath("cities_wiki\\{}.txt".format(self.cities_ADT[i].name)),
                          encoding='utf-8') as f:
                    self.cities_ADT[i].extra_data["wiki information"] = f.read()
            except:
                pass

            self.add_city(self.cities_ADT[i])

    def last_city(self):
        """

        :return: last added elem in ADT
        """
        return self.app_cities.peek()

    def remove_all(self):
        """
        Remove all cities
        :return: None
        """
        self.app_cities.clear()

    def is_empty(self):
        """
        Check if ADT is empty
        :return: bool
        """
        return self.app_cities.is_empty()

    def pop(self):
        """
        Delete last element and return it
        :return: Place
        """
        return self.app_cities.pop()

    def __len__(self):
        """
        Length of Stack
        :return:
        """
        return len(self.app_cities)

