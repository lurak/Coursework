from unittest import TestCase
from ADT.resortInfo import ResortsInfo


class TestResortsInfo(TestCase):
    def setUp(self):
        self.resorts = ResortsInfo(3)

    def test_create(self):
        self.resorts.create("files\\places.json", "cultural resorts")
        self.assertEqual(str(self.resorts), "Colmar\nSenglea\nAlberobello\n")

