from ADT.resortInfo import ResortsInfo, PlaceInfo
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
PLACES = PlaceInfo(1257)
CURRENCIES = PlaceInfo(423)

i = 0
with open(os.path.abspath("SimpleSite\\files\\ids.txt"), encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        PLACES[i] = line[:-1]
        i += 1

i = 0
with open(os.path.abspath("SimpleSite\\files\\currencies.txt"), encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break

        CURRENCIES[i] = line[:-1]
        i += 1

DATES = []


d1 = datetime.datetime.today()
d2 = datetime.date.today() + datetime.timedelta(365/12)
days = [d1 + datetime.timedelta(days=x) for x in range(30 + 1)]
for day in days:
    DATES.append(day.strftime('%d/%m/%Y'))
