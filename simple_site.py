import os
from datetime import date
import json
from flask import Flask, render_template, request
from SimpleSite.constData import DATES
from ADT.appropriatePlaces import AppropriatePlaces
from SimpleSite.constData import RESORTS, PLACES, CURRENCIES
from SimpleSite.optimal_places import choose_cities
from extra_modules.place import Place
from extra_modules.price import Price
from SimpleSite.map_cities import get_map


app = Flask(__name__)


@app.route('/')
def index():
    try:
        dates = DATES
        currencies = CURRENCIES
        info = PLACES
        return render_template("index.html", currencies=currencies, info=info, dates=dates)
    except:
        return render_template("Error.html")


@app.route('/propositions', methods=["POST"])
def propositions():
    try:
        city_id = request.form.get("city")

        price = Price(request.form.get("price"), request.form.get("Currency"))

        arr_date = request.form.get("arr_date").split('/')
        dep_date = request.form.get("dep_date").split('/')

        resortType = request.form.get("resort_type")
        delta = date(int(dep_date[2]), int(dep_date[1][-1]), int(dep_date[0])) - \
                      date(int(arr_date[2]), int(arr_date[1][-1]), int(arr_date[0]))
        days_number = delta.days if delta.days <= 5 else 5


        appropriatePlaces = AppropriatePlaces(RESORTS[resortType], days_number)

        coefficient = price.currency_coefficient("USD")
        info = []

        while not appropriatePlaces.is_empty():
            place = appropriatePlaces.pop()

            if place.id is not None:

                ticketsInfo = choose_cities(int(city_id), int(place.id), "/".join(arr_date),
                                            float(price.price)*coefficient,
                                            coefficient, price.currency)
            else:
                ticketsInfo = []

            info.append((ticketsInfo,
                         place.extra_data["picture"],
                         place.extra_data["wiki information"],
                         place.id,
                         place.latitude,
                         place.longitude,
                         place.name))

        new_price = price.price*coefficient
        return render_template("propositions.html", price=new_price, info=info)
    except:
        return render_template("Error.html")


@app.route('/propositions/city', methods=["POST"])
def city():
    try:
        info = request.form.get("picture").split("**")
        map_map = True
        try:
            city = Place(info[6], latitude=float(info[4]), longitude=float(info[5]))

            get_map(city, os.path.abspath("templates\\map.html"))
        except:
            map_map = False

        return render_template("city.html", info=info, map=map_map)
    except:
        return render_template("Error.html")


@app.route('/propositions/city/tickets', methods=["POST"])
def tickets():
    try:
        ticket = json.loads(request.form.get("tickets").replace("'", '"'))

        return render_template("tickets.html", tickets=ticket)
    except:
        return render_template("Error.html")


if __name__ == "__main__":
    app.run(debug=True)
