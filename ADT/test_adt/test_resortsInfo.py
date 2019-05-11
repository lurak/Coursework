from unittest import TestCase
from ADT.resortInfo import ResortsInfo


class TestResortsInfo(TestCase):
    def setUp(self):
        self.resorts = ResortsInfo(5)

    def test_create(self):
        self.resorts.create("places.json", "cultural resorts")
        self.assertEqual(str(self.resorts), "Colmar\nSenglea\nEz\nAlberobello\nFreiburg\n")

