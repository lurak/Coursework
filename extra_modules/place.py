import wikipedia
from math import acos, radians, sin, cos

from geopy.geocoders import Nominatim
import re


class Place:
    def __init__(self, name, id=None, extra_data={}, latitude=None, longitude=None):
        """Class for place representation"""
        self.name = name
        self.extra_data = extra_data
        self.latitude = latitude
        self.longitude = longitude
        self.id = id

    def get_coordinates(self):
        """
        Get coordinates of place
        :return:
        """
        geolocator = Nominatim(user_agent="specify_your_app_name_here")
        location = geolocator.geocode(self.name)
        self.latitude, self.longitude = location.latitude, location.longitude

    def distance(self, place):
        """

        :param place: Place
        :return: Distance between two places
        """
        slat = radians(self.latitude)
        slon = radians(self.longitude)
        elat = radians(place.latitude)
        elon = radians(place.longitude)

        dist = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
        return dist

    def wiki_information(self):
        """
        Add wiki information about place
        :return: None
        """

        try:

            content = wikipedia.page(self.name).content
            content = content[:content.index('==')]

            content = content.replace(
                re.findall("\([^)]+\)", content)[0], ""
                )

            self.extra_data["wiki information"] = content

        except:
            import requests


            info = re.findall('<p><b>.*', requests.get("https://en.wikipedia.org/wiki/{}".format(self.name)).text)[0]
            staff = re.findall('(<.*?>)', info)
            for tag in staff:
                info = info.replace(tag, "")
            self.extra_data['wiki information'] = info

    def __eq__(self, place):
        """
        Check if places are equel
        :param place:
        :return:
        """
        return self.name == place.name

    def __str__(self):
        """
        City Name
        :return:
        """
        return self.name
