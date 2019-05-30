import os
from unittest import TestCase, main
from ADT.resortInfo import ResortsInfo
from ADT.appropriatePlaces import AppropriatePlaces
from extra_modules.weather_analysis import Weather
from extra_modules.place import Place


class TestAppropriatePlaces(TestCase):
    def setUp(self):
        resorts = ResortsInfo(3)
        resorts.create("files\\places.json", "cultural resorts")

        self.cities = ['Colmar', 'Senglea', 'Alberobello']
        self.init_path = os.path.abspath("files\\initial_weather.json")
        self.final_path = os.path.abspath("files\\final_weather.json")
        self.app_places = AppropriatePlaces(resorts, 2, self.init_path, self.final_path)

    def test_check_city(self):
        self.assertEqual(self.app_places.check_city(Place("Berlin")), Weather("Berlin", 2,
                                                                              self.init_path,
                                                                              self.final_path).good_weather())

    def test_add_city(self):
        self.app_places.add_city(Place("Berlin"))
        if Weather("Berlin", 2, self.init_path, self.final_path).good_weather():
            self.assertEqual(str(self.app_places.last_city()), "Berlin")

    def test_create(self):
        good_cities = []
        for city in self.cities:
            if Weather(city, 2, self.init_path, self.final_path).good_weather():
                good_cities.append(city)

        self.assertEqual(len(self.app_places), len(good_cities))
        for i in range(len(good_cities) - 1, -1, -1):
            self.assertEqual(good_cities[i], str(self.app_places.pop()))

    def test_remove_all(self):
        self.app_places.remove_all()
        self.assertEqual(len(self.app_places), 0)

    def test_is_empty(self):
        self.app_places.remove_all()
        self.assertEqual(self.app_places.is_empty(), True)

    def test_pop(self):
        self.app_places.add_city(Place("Berlin"))

        if Weather("Berlin", 2, self.init_path, self.final_path).good_weather():
            self.assertEqual(str(self.app_places.pop()), "Berlin")
        if self.app_places.is_empty():
            self.assertEqual(self.app_places.pop(), None)
        else:
            length = len(self.app_places) - 1
            self.app_places.pop()
            self.assertEqual(len(self.app_places), length)


if __name__ == "__main__":
    main()
