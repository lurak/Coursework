import os

from omio.omio import get_search_id, get_tickets_json, tickets_info


def choose_cities(arr_id, dep_id, date, price, coefficient, currency="UAH"):
    """

    Return dictionaty with tickets for transport

    :param arr_id: arrival city id
    :param dep_id: departure city id
    :param date: date of arrival
    :param price: max price of travel (0 = infinity)
    :param coefficient: coefficient of currency
    :param currency: current currency
    :return: dict
    """
    info = []
    while True:
        try:
            search_id = get_search_id(arr_id, dep_id, date=date)
            break
        except:
            return info
    k = 0
    while True:
        if k == 4:
            break
        try:

            get_tickets_json(os.path.abspath("SimpleSite\\files\\initial_tickets.json"), search_id)
            dct = tickets_info(inpath=os.path.abspath("SimpleSite\\files\\initial_tickets.json"),
                               search_id=search_id,
                               outpath=os.path.abspath("SimpleSite\\files\\final_tickets.json"),
                               price=price)

            for num in dct.values():

                info.append({"Departure time": "{}, {}".format(num["departureTime"][5:10], num["departureTime"][11:16]),
                             "Arrival time": "{}, {}".format(num["ar_time"][5:10], num["ar_time"][11:16]),
                             "Number of stops": num["stops"],
                             "Company:": num["companyName"],
                             "Price": str(round(num["price"] / coefficient, 2)) + currency,
                             "Transport": num["mode"],
                             "Departure station": num["stations_dep"][0]["name"],
                             "Arrival station": num["stattions_ar"][-1]["name"],
                             "Departure city": num["stations_dep"][0]["cityName"],
                             "Arrival city": num["stattions_ar"][-1]["cityName"],
                             "url": num["url"],
                             "City Code": num["stattions_ar"][-1]["iataCode"]})


            break
        except:

            k += 1

    return info



