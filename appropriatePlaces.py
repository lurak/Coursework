from linkedList import LinkedList
from weather_analysis import Weather
from place import Place


class AppropriatePlaces:
    def __init__(self, cities_ADT, days):
        """

        :param cities_ADT: ResortInfo
        :param days: int
        """
        self.app_cities = LinkedList()
        self.cities_ADT = cities_ADT
        self.days = days
        try:
            self.create()
        except:
            print("OK")

    def check_city(self, city):
        """

        :param city: Place
        :return: check if place is optimal
        """
        if not isinstance(city, Place):
            raise TypeError("city type should be Place")
        weather = Weather(city.name, self.days)
        return weather.good_weather()

    def add_city(self, city):
        """
        Add city to ADT

        :param city: Place
        :return: None
        """
        if self.check_city(city):
            self.app_cities.add(city)

    def create(self):
        """
        Fill ADT with optimal cities
        :return: None
        """
        for i in range(len(self.cities_ADT)):
            self.cities_ADT[i].wiki_information()
            self.add_city(self.cities_ADT[i])

    def delete(self, value):
        """
        Delete city from ADT
        :param value: Place
        :return: None
        """
        self.app_cities.delete(value)

    def remove_all(self):
        """
        Remove all cities
        :return: None
        """
        self.app_cities.remove_all()

    def is_empty(self):
        """
        Check if ADT is empty
        :return: bool
        """
        return self.app_cities.empty()

    def pop(self):
        """
        Delete last element and return it
        :return: Place
        """
        element = self.app_cities._head.item
        self.app_cities._head = self.app_cities._head.next
        self.app_cities._size -= 1
        return element

    def __str__(self):
        """
        View of ADT
        :return: str
        """
        return str(self.app_cities)
