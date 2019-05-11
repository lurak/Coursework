from flask import Flask, render_template, request
from SimpleSite.place import Place
from SimpleSite.price import Price
#from SimpleSite.omio import cities_ids, get_search_id, get_tickets_json, tickets_info
#from SimpleSite.map_cities import get_map
from Const_data.constData import RESORTS
from ADT.appropriatePlaces import AppropriatePlaces

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/price', methods=["POST"])
def price():
    city = Place(request.form.get("city")).name
    price = Price(request.form.get("price"), request.form.get("Currency"))
    indate = "{}/{}/{}".format(request.form.get("inday"),
                               request.form.get("inmonth"),
                               request.form.get("inyear"))
    outdate = "{}/{}/{}".format(request.form.get("outday"),
                                request.form.get("outmonth"),
                                request.form.get("outyear"))
    resortType = request.form.get("resort_type")
    days_number = int(request.form.get("outday")) - int(request.form.get("inday"))
    appropriatePlaces = AppropriatePlaces(RESORTS[resortType], days_number)
    #cityId = cities_ids(city, city, "files\\ids.txt")
    #coefficient = price.currency_coefficient("USD")
    coefficient = 0.037216
    # while True:
    #     try:
    #         search_id = get_search_id(ids[0], ids[1], date=date)
    #         break
    #     except:
    #         pass
    # while True:
    #     try:
    #
    #         get_tickets_json("files\\initial_tickets.json", search_id)
    #         dct = tickets_info(inpath="files\\initial_tickets.json",
    #                            search_id=search_id,
    #                            outpath="files\\final_tickets.json")
    #         break
    #     except:
    #         pass
    # info = []
    # place_in = Place(incity)
    # place_out = Place(outcity)
    # place_in.get_coordinates()
    # place_out.get_coordinates()
    # get_map([place_in, place_out], "templates\\map.html", location=list(place_out.coordinates))
    # for num in dct.values():
    #     info.append(["Departure time: {}".format(num["departureTime"]),
    #                  "Arrival time: {}".format(num["ar_time"]),
    #                  "Number of stops: {}".format(num["stops"]),
    #                  "Company: {}".format(num["companyName"]),
    #                  "Price: {}".format(str(round(num["price"]/coefficient, 2))),
    #                  "Transport: {}".format(num["mode"]),
    #                  "Departure station: {}".format(num["stations_dep"][0]["name"]),
    #                  "Arrival station: {}".format(num["stattions_ar"][0]["name"]),
    #                  num["url"]])
    new_price = price.price*coefficient
    return render_template("price.html", price=new_price, info=appropriatePlaces)


if __name__ == "__main__":
    app.run(debug=True)
