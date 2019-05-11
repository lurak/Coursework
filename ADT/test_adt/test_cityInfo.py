from unittest import TestCase, main
from ADT.cityInfo import CityInfo


class TestCityInfo(TestCase):
    def setUp(self):
        self.cities = CityInfo(5)

    def test_create(self):
        self.cities.create("cities.txt")
        self.assertEqual(str(self.cities), "Gdańsk\nSgonico\nLviv\nBerlin\nLondon\n")
