from datetime import datetime

from flask import current_app, render_template


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


def earthquakes_page():
    db = current_app.config["db"]
    earthquakes = db.get_earthquakes()
    return render_template("earthquakes.html", earthquakes=sorted(earthquakes))


def earthquake_page(earthquake_key):
    db = current_app.config["db"]
    earthquake = db.get_earthquake(earthquake_key)
    return render_template("earthquake.html", earthquake=earthquake)
