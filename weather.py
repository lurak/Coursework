import requests
import json


def get_weather_json(place, path):
    """
    (str,str) -> None


    Return the json with weather forecast

    """
    url = "http://api.openweathermap.org/data/2.5/forecast?q=place&APPID=31b1ca6622c183dd92fb23a72f492b36"
    url = url.replace("place", place)
    text = requests.get(url)
    text = text.text
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json.loads(text), f, indent=4)


def get_info_from_json(inpath, outpath):
    """
    (str,str) -> None 
    Take from jsom all kind of temperature and date.
    """

    f = open(inpath, encoding='utf-8')
    info = f.read()
    info = json.loads(info)
    f.close()
    dct = {}
    for el in info["list"]:
       dct[el["dt_txt"]] = {"temp_min": float(el["main"]["temp_min"]) - 273,
                             "temp_max": float(el["main"]["temp_min"]) - 273,
                             "weather": el["weather"][0]["description"] + ", " +
                                        el["weather"][0]["main"]}
    with open(outpath, 'w', encoding='utf-8') as f:
        json.dump(dct, f, indent=4)


if __name__ == "__main__":
    get_weather_json("Durban", "w.json")
    get_info_from_json("w.json", "need.json")