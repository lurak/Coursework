import json
import re

def json_reader():
    """
    Create a json file with some resorts.
    """
    with open("data.json", encoding='utf-8') as f:
        dct = json.loads(f.read(), encoding='utf-8')
    ski = dct["ski resorts"]
    cul = dct["cultural resorts"]
    sea = {}
    ski = txt_process(ski, "ski_resorts.txt")
    cul = txt_process(cul, "cultural_resorts.txt")
    sea = txt_process(sea, "sea_resorts.txt")
    dct["ski resorts"] = ski
    dct["cultural resorts"] = cul
    dct["sea resorts"] = sea
    json_writer(dct)


def txt_process(dct, path):
    """
    Take name of resorts from txt file.
    """
    with open(path, encoding="utf-8") as f:
        for line in f:
            name = re.findall('(.*),', line)
            dct[name[0]] = name[0]
    return dct


def json_writer(dct):
    """
    Write these resorts to the json file. 
    """
    with open('data.json', 'w') as fi:
         json.dump(dct, fi, indent=4)


if __name__ == "__main__":
    json_reader()
