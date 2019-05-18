import requests
import json
import urllib.parse
import re
import pprint


def get_tickets_json(path, search_id):
    """
    :param path: str
    :param search_id: int
    :return: None

    Return the json with tickets

    """
    url = "https://www.omio.com/GoEuroAPI/rest/api/v5/results"
    params = {
        'direction': 'outbound',
        'easy': '0',
        'eoff': 'on',
        'exclude_offsite_bus_results': True,
        'include_segment_positions': True,
        'search_id': search_id,
        'sort_by': 'updateTime',
        'sort_variants': 'onsiteDepartureTime, outboundDepartureTime, outboundPrice, price, smart, traveltime',
        'spl_tren': 'v1',
        'updated_since': 0,
        'use_recommendation': True,
        'use_stats': True
    }
    text = requests.get(url, params=params)
    text = text.text
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(json.loads(text), file, indent=4)


def tickets_info(inpath, search_id, outpath, price=0):
    """

    :param inpath: str
    :param search_id: int
    :param outpath: str
    :param price: float
    :return: dict

    Return the dict of tickets info
    """
    with open(inpath,  encoding='utf 8') as f:
        js = json.loads(f.read())
    dct = {}
    for el in js["outbounds"]:
        el = js["outbounds"][el]
        if price == 0 or float(el["price"])/100 <= price:
            segments = el["segments"]
            lst_dep = []
            lst_ar = []
            for segment in segments:
                lst_dep.append(js["positions"][js["segmentDetails"][str(segment)]["departurePosition"]])
                lst_ar.append(js["positions"][js["segmentDetails"][str(segment)]["arrivalPosition"]])

            for i in js["stats"]["companies"][el["mode"]]:
                if i["id"] == el["companyId"]:
                    companyName = i["name"]
            dct[el["journeyId"]+'/'+el["outboundId"]] = {"departureTime": el["departureTime"],
                      "ar_time": el["arrivalTime"],
                      "stops": el["stops"],
                      "companyName": companyName,
                      "cID": el["companyId"],
                      "price": el["price"]/100,
                      "segment": el["segments"],
                      "mode": el["mode"],
                      "stations_dep": lst_dep,
                      "stattions_ar": lst_ar,
                      "url": ticket_url(search_id, el["journeyId"]+'/'+el["outboundId"], el["mode"])}
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(json.dumps(dct, indent=4))
    return dct


def get_search_id(departure_id, arrival_id, date):
    """

    :param departure_id: str
    :param arrival_id: str
    :param date: str
    :return: int

    Return search id
    """
    url = "https://www.omio.com/growth/search-trigger/search"
    data = {'departure_fk': departure_id,
            'arrival_fk': arrival_id,
            'departure_date': date,
            'adults': 1,
            'children': 0,
            'infants': 0,
            'youths': 0,
            'passengerAges': '[object Object]',
            'user_id': '8abe6dba-7c5e-42ed-89b5-1fc078db58e6',
            'user_currency': 'USD',
            'user_domain': 'com',
            'user_locale': 'en',
            'travel_mode': 'train',
            'abTestParameters': None,
            'srpQueryParams': None,
            'is_rebrand': True
            }
    urllib.parse.urlencode(data)
    req = requests.get(url, params=data)
    #print(req.url)
    return re.findall("/[A-Z\d]+/", req.url)[0][1:-1]


def cities_ids(departure_city, arrival_city, places):
    """

    :param departure_city: str
    :param arrival_city: str
    :param places: str
    :return: tuple

    Return the tuple of ids of cities
    """

    k = 0
    departure_id = 0
    arrival_id = 0
    for line in places:
        if k == 2:
            break
        line = line.split(', ')
        if arrival_city == line[1]:
            arrival_id = line[0][line[0].index('.')+1:]
            k += 1
        elif departure_city == line[1]:
            departure_id = line[0][line[0].index('.')+1:]
            k += 1

    return departure_id, arrival_id


def ticket_url(search_id, ids, mode):
    """

    :param search_id: int
    :param ids: list
    :param mode: str
    :return: str

    Return the url of ticket
    """
    journeyId = ids[:ids.index('/')]
    outboundId = ids[ids.index('/')+1:]
    return "https://www.omio.com/search-frontend/journey/{}/{}/{}/{}".format(mode,
                                                                             journeyId,
                                                                             str(search_id),
                                                                             outboundId)


