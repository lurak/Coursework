from math import acos, radians, sin, cos

from geopy.geocoders import Nominatim


class Place:
    def __init__(self, name, id=None, extra_data=None, latitude=None, longitude=None):
        self.name = name
        self.extra_data = extra_data
        self.latitude = latitude
        self.longitude = longitude
        self.id = id

    def get_coordinates(self):
        geolocator = Nominatim(user_agent="specify_your_app_name_here")
        location = geolocator.geocode(self.name)
        self.latitude, self.longitude = location.latitude, location.longitude

    def distance(self, place):
        slat = radians(self.latitude)
        slon = radians(self.longitude)
        elat = radians(place.latitude)
        elon = radians(place.longitude)

        dist = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
        return dist

    def __str__(self):
        return self.name
