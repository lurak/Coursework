import requests
import json


def convert_currency(cur1, cur2, value):
    """
    (str,str,number) -> number

    Converte value of one currency to another with help of API. 
    """
    url = "https://free.currencyconverterapi.com/api/v6/convert?q=currencies&compact=ultra&apiKey=5cf74c565258dbb237af"
    params = cur1 + '_' + cur2
    url = url.replace("currencies", params)
    value = float(json.loads(requests.get(url).text)[params])*value
    return value


if __name__ == "__main__":
    print(convert_currency("UAH", "USD", 500))



