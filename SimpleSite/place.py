from geopy.geocoders import Nominatim


class Place:
    def __init__(self, name, coordinates=None):
        self.name = name
        self.coordinates = coordinates

    def get_coordinates(self):
        geolocator = Nominatim(user_agent="specify_your_app_name_here")
        location = geolocator.geocode(self.name)
        self.coordinates = (location.latitude, location.longitude)
        print(self.coordinates)

    def distance(self, city):
        pass


