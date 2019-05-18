import requests


def booking_url(code):
    url = "https://www.booking.com/searchresults.html?dest_type=city;iata=code"
    data = {
        "checkin_year": 2019,
        "checkin_month": 5,
        "checkin_monthday": 18,
        "checkout_year": 2019,
        "checkout_month": 5,
        "checkout_monthday": 25,
        "group_adults": 2,
        "group_children": 0,
        "no_rooms": 1,
        "ss_raw": "Riga",

        "dest_type": "city",
        "iata": "REX"
    }

    return url.replace("code", code)
