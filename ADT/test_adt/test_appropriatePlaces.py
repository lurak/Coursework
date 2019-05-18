from unittest import TestCase, main
from ADT.resortInfo import ResortsInfo
from ADT.appropriatePlaces import AppropriatePlaces
from extra_modules.weather_analysis import Weather
from extra_modules.place import Place


class TestAppropriatePlaces(TestCase):
    def setUp(self):
        resorts = ResortsInfo(5)
        resorts.create("places.json", "cultural resorts")
        self.cities = ['Freiburg', 'Alberobello', 'Ez', 'Sengelea', 'Colmar']
        self.app_places = AppropriatePlaces(resorts, 2)

    def test_check_city(self):
        self.assertEqual(self.app_places.check_city(Place("Berlin")), Weather("Berlin", 2).good_weather())

    def test_add_city(self):
        if Weather("Berlin", 2).good_weather():
            places = str(self.app_places) + '->Berlin'
        else:
            places = str(self.app_places)
        self.app_places.add_city(Place("Berlin"))
        self.assertEqual(str(self.app_places), places)

    def test_create(self):
        string = ""

        for city in self.cities:
            if Weather(city, 2).good_weather():
                string += city + '->'
        string = string[:-2]
        self.assertEqual(str(self.app_places), string)

    def test_delete(self):
        string = str(self.app_places)
        cities = string.split('->')
        self.app_places.delete(Place(cities[0]))
        self.assertEqual(str(self.app_places), "->".join(cities[1:]))

    def test_remove_all(self):
        self.app_places.remove_all()
        self.assertEqual(str(self.app_places), "")

    def test_is_empty(self):
        self.app_places.remove_all()
        self.assertEqual(self.app_places.is_empty(), True)

    def test_pop(self):
        cities = str(self.app_places).split('->')
        self.assertEqual(str(self.app_places.pop()), cities[-1])
        self.assertEqual(str(self.app_places), '->'.join(cities[:-1]))


if __name__ == "__main__":
    main()
