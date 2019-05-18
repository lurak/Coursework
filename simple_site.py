import time
from datetime import date
import json
from flask import Flask, render_template, request
from SimpleSite.constData import DATES
from ADT.appropriatePlaces import AppropriatePlaces
from SimpleSite.constData import RESORTS, PLACES
from SimpleSite.optimal_places import choose_cities
from extra_modules.place import Place
from extra_modules.price import Price


app = Flask(__name__)


@app.route('/')
def index():
    dates = DATES
    currencies = ['UDS', "UAH"]
    info = PLACES
    return render_template("index.html", currencies=currencies, info=info, dates=dates)


@app.route('/fle', methods=["POST"])
def fle():
    city = Place(request.form.get("city")).name
    price = Price(request.form.get("price"), request.form.get("Currency"))
    arr_date = request.form.get("arr_date").split('/')
    dep_date = request.form.get("dep_date").split('/')

    resortType = request.form.get("resort_type")
    delta = date(int(dep_date[2]), int(dep_date[1][-1]), int(dep_date[0])) - \
                  date(int(arr_date[2]), int(arr_date[1][-1]), int(arr_date[0]))
    days_number = delta.days if delta.days <= 5 else 5

    start = time.time()
    appropriatePlaces = AppropriatePlaces(RESORTS[resortType], days_number)

    coefficient = price.currency_coefficient("USD")
    info = []

    while not appropriatePlaces.is_empty():
        place = appropriatePlaces.pop()
        ticketsInfo = choose_cities(city, str(place), "/".join(arr_date), float(price.price)*coefficient, coefficient)
        info.append((ticketsInfo,
                     place.extra_data["picture"],
                     place.extra_data["wiki information"]))

    # place_in.get_coordinates()
    # place_out.get_coordinates()
    # get_map([place_in, place_out], "templates\\map.html", location=list(place_out.coordinates))

    new_price = price.price*coefficient
    return render_template("fle.html", price=new_price, pictures=info)


@app.route('/fle/final', methods=["POST"])
def final():
    pictures = request.form.get("picture").split('**')

    return render_template("final.html", pictures=pictures)


@app.route('/fle/final/tickets', methods=["POST"])
def tickets():
    ticket = json.loads(request.form.get("tickets").replace("'", '"'))

    return render_template("tickets.html", tickets=ticket)

