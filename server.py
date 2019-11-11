from flask import Flask

import views
from database import Database
from earthquake import earthquake


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/earthquake", view_func=views.earthquake_page)

    db = Database()
    db.add_earthquake(earthquake("Istanbul", year=2019))
    app.config["db"] = db

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
