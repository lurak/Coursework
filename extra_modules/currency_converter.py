import requests
import json


def convert_currency(cur1, cur2, value):
    """

    :param cur1: str
    :param cur2: str
    :param value: number
    :return: number

    Convert value of one currency to another


    """
    url = "https://free.currencyconverterapi.com/api/v6/convert?q=currencies&compact=ultra&apiKey=5cf74c565258dbb237af"
    params = cur1 + '_' + cur2
    url = url.replace("currencies", params)
    value = float(json.loads(requests.get(url).text)[params])*value
    return value




