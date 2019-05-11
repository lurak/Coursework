import json
from weather_funcs import get_weather_json, get_info_from_json


class Weather:
    def __init__(self, place, days):
        """

        :param place: str
        :param days: int1
        """
        self.place = place
        self.weather_json()
        self.js = self.reader()
        self.days = days

    def weather_json(self):
        """
        Create json with weather
        :return: None
        """
        try:
            get_weather_json(self.place, "initial.json")
            get_info_from_json("initial.json", "weather.json")
        except:
            pass

    @staticmethod
    def reader():
        """
        Return dict with weather
        :return: dict
        """
        with open("weather.json") as f:
            return json.load(f)

    def get_season(self):
        """

        Return season by month

        :return: str
        """
        keys = [key for key in self.js]
        season = keys[0][5:7]
        if season == '01' or season == '02' or season == '12':
            return 'winter'
        elif season == '03' or season == '04' or season == '05':
            return 'spring'
        elif season == '06' or season == '07' or season == '08':
            return 'summer'
        elif season == '09' or season == '10' or season == '11':
            return 'autumn'

    def good_weather(self):
        """
        Check if weather is optimal
        :return: bool
        """
        condition = True
        keys = [key for key in self.js]
        for i in range(8 * self.days):
            data = self.js[keys[i]]
            if 'Rain' in data['weather']:
                condition = False
                break
        counter = 0
        count = 0
        temperature = list()
        avarage = list()
        av = 0
        if condition:
            for j in range(len(keys)):
                if counter == self.days*4:
                    break
                if '09:' in keys[j] or '12:' in keys[j] or '15:' in keys[j] or "18:" in keys[j]:
                     temperature.append((self.js[keys[j]]['temp_max'] + self.js[keys[j]]['temp_min'])/2)
                     counter += 1
        else:
            return False
        for o in range(len(temperature)):
            count += 1
            if count % 4 == 0:
                avarage.append(av/4)
                av = 0
            av += temperature[o]
        condition = self.avarage_throught_days(avarage)
        return condition

    def avarage_throught_days(self, lst):
        """
        Count the average temperature and return if this temperature is suitable for this season. 
        :param lst: list
        :return: bool
        """
        season = self.get_season()
        if season == "winter":
            for i in range(len(lst)):
                if lst[i] <= -15:
                    return False
        elif season == "spring":
            for i in range(len(lst)):
                if lst[i] >= 25 or lst[i] <= 5:
                    return False
        elif season == "summer":
            for i in range(len(lst)):
                if lst[i] >= 30 or lst[i] <= 10:
                    return False
        elif season == "autumn":
            for i in range(len(lst)):
                if lst[i] >= 25 or lst[i] <= 10:
                    return False
        return True
