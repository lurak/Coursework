from resortInfo import ResortsInfo, PlaceInfo
import datetime


CULTURAL_RESORTS_NUMBER = 58
SEA_RESORTS_NUMBER = 30
SKI_RESORTS_NUMBER = 33
CULTURAL_RESORTS = ResortsInfo(CULTURAL_RESORTS_NUMBER)
SEA_RESORTS = ResortsInfo(SEA_RESORTS_NUMBER)
SKI_RESORTS = ResortsInfo(SKI_RESORTS_NUMBER)
CULTURAL_RESORTS.create("data.json", "cultural resorts")
SEA_RESORTS.create("data.json", "sea resorts")
SKI_RESORTS.create("data.json", "ski resorts")
RESORTS = {"cultural resorts": CULTURAL_RESORTS, "sea resorts": SEA_RESORTS, "ski resorts": SKI_RESORTS}
PLACES = PlaceInfo(1257)
i = 0
with open("ids.txt", encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
            break
        PLACES[i] = line
        i += 1

DATES = []


d1 = datetime.datetime.today()
d2 = datetime.date.today() + datetime.timedelta(365/12)
days = [d1 + datetime.timedelta(days=x) for x in range(30 + 1)]
for day in days:
    DATES.append(day.strftime('%d/%m/%Y'))
