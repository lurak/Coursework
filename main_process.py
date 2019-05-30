from ADT.appropriatePlaces import AppropriatePlaces
from datetime import date
from SimpleSite.constData import RESORTS
from SimpleSite.optimal_places import choose_cities
from extra_modules.price import Price
from omio.omio import cities_ids
from SimpleSite.constData import PLACES
import pprint

pp = pprint.PrettyPrinter(indent=2)
resort_type = input("input cultural resorts, sea resorts or ski resorts: ")
arr_date = input("input arrival date (date-month-year): ").split('-')
dep_date = input("input departure date: ").split('-')
currency = input("Enter currency(for example UAH): ")
price = Price(int(input("Enter maximal price: ")), currency)
delta = date(int(dep_date[2]), int(dep_date[1][-1]), int(dep_date[0])) - \
        date(int(arr_date[2]), int(arr_date[1][-1]), int(arr_date[0]))

# If delta of days is greater than five delta will be five because of limit weather api
days = delta.days if delta.days <= 5 else 5
appropriatePlaces = AppropriatePlaces(RESORTS[resort_type], days)
info = []
coefficient = price.currency_coefficient("USD")
while not appropriatePlaces.is_empty():
    place = appropriatePlaces.pop()
    print("---------------------------------------------------")
    print(place)
    city_id = cities_ids(place.name, PLACES)
    if place.id is not None:

        ticketsInfo = choose_cities(int(city_id), int(place.id), "/".join(arr_date),
                                    float(price.price) * coefficient,
                                    coefficient, price.currency)
    else:
        ticketsInfo = []

    info.append((ticketsInfo,

                 place.name))
    pp.pprint(info)

