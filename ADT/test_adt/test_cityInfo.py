from unittest import TestCase

from ADT.cityInfo import CityInfo


class TestResortsInfo(TestCase):
    def setUp(self):
        self.cities = CityInfo(3)

    def test_create(self):
        self.cities.create("files\\cities.txt")

        self.assertEqual(str(self.cities).split('\n'), ["376073, Aachen, Germany, DE, 6.08342, 50.77664",
                                                        "16883149, Ab, Germany, DE, 9.135555400000001, 49.9806625",
                                                        "380037, Aberdeen, United Kingdom, GB, -2.09814, 57.14369"])

