from ADT.resortInfo import ResortsInfo


CULTURAL_RESORTS_NUMBER = 58
SEA_RESORTS_NUMBER = 30
SKI_RESORTS_NUMBER = 33
CULTURAL_RESORTS = ResortsInfo(CULTURAL_RESORTS_NUMBER)
SEA_RESORTS = ResortsInfo(SEA_RESORTS_NUMBER)
SKI_RESORTS = ResortsInfo(SKI_RESORTS_NUMBER)
CULTURAL_RESORTS.create("C:\\Users\\user\\PycharmProjects\\Coursework\\Last_Module\\data.json", "cultural resorts")
SEA_RESORTS.create("C:\\Users\\user\\PycharmProjects\\Coursework\\Last_Module\\data.json", "sea resorts")
SKI_RESORTS.create("C:\\Users\\user\\PycharmProjects\\Coursework\\Last_Module\\data.json", "ski resorts")
RESORTS = {"cultural resorts": CULTURAL_RESORTS, "sea resorts": SEA_RESORTS, "ski resorts": SKI_RESORTS}
