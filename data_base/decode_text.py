import json
import pprint


def decode(string):
    for char in string:
        char = chr(ord(char))
    return string


with open("data.json", encoding='utf-8') as f:
    dct = json.loads(f.read(), encoding='utf-8')
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(dct)
