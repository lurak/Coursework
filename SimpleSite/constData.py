from ADT.cityInfo import CityInfo
from ADT.resortInfo import ResortsInfo

import datetime
import os


CULTURAL_RESORTS_NUMBER = 52
SEA_RESORTS_NUMBER = 27
SKI_RESORTS_NUMBER = 13
CULTURAL_RESORTS = ResortsInfo(CULTURAL_RESORTS_NUMBER)
SEA_RESORTS = ResortsInfo(SEA_RESORTS_NUMBER)
SKI_RESORTS = ResortsInfo(SKI_RESORTS_NUMBER)
CULTURAL_RESORTS.create(os.path.abspath("SimpleSite\\files\\resorts.json"), "cultural resorts")
SEA_RESORTS.create(os.path.abspath("SimpleSite\\files\\resorts.json"), "sea resorts")
SKI_RESORTS.create(os.path.abspath("SimpleSite\\files\\resorts.json"), "ski resorts")
RESORTS = {"cultural resorts": CULTURAL_RESORTS, "sea resorts": SEA_RESORTS, "ski resorts": SKI_RESORTS}
PLACES = CityInfo(1257)
PLACES.create(os.path.abspath("SimpleSite\\files\\ids.txt"))
CURRENCIES = CityInfo(423)
CURRENCIES.create(os.path.abspath("SimpleSite\\files\\currencies.txt"))


DATES = []


d1 = datetime.datetime.today()
d2 = datetime.date.today() + datetime.timedelta(365/12)
days = [d1 + datetime.timedelta(days=x) for x in range(30 + 1)]
for day in days:
    DATES.append(day.strftime('%d/%m/%Y'))

