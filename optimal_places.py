from omio import get_search_id, get_tickets_json, tickets_info, cities_ids

from constData import PLACES


def choose_cities(city1, city2, date, price, coefficient, currency="UAH"):
    ids = cities_ids(city1, city2, PLACES)

    info = []
    while True:
        try:
            search_id = get_search_id(ids[0], ids[1], date=date)
            break
        except:
            return info
    k = 0
    while True:
        if k == 4:
            break
        try:

            get_tickets_json("initial_tickets.json", search_id)
            dct = tickets_info(inpath="initial_tickets.json",
                               search_id=search_id,
                               outpath="final_tickets.json",
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

    # place_in = Place(city1)
    # place_out = Place(city2)
    # place_in.get_coordinates()
    # place_out.get_coordinates()
    # get_map([place_in, place_out], "templates\\map.html", location=list(place_out.coordinates))

    return info



