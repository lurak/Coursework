from unittest import TestCase
from ADT.placeInfo import PlaceInfo
from extra_modules.place import Place


class TestPlaceInfo(TestCase):
    def setUp(self):
        self.places = PlaceInfo(2)

    def test_setitem(self):
        self.places[0] = Place("Berlin")
        self.assertEqual(str(self.places), "Berlin\nNone\n")

    def test_getitem(self):
        self.places[0] = Place("Durban")
        self.assertEqual(str(self.places[0]), "Durban")

    def test_len(self):
        self.places[0] = Place("Durban")
        self.assertEqual(len(self.places), 1)