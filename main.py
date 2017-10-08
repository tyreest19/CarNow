from flask import Flask, render_template
from Model import database
app = Flask(__name__, template_folder='View/templates/', static_folder='View')
app.config['DEBUG'] = False


@app.route("/")
def home():
    # return "Welcome to CarNow"
    return render_template("index.html")

@app.route("/map.html")
def parkingLot():
    # return "Map Page"
    return render_template("map.html")

@app.route("/search")
def searchCar():
    """Page will allow users to search for a car"""
    database.read()

def presenetCar():
    """This page will load all the default care info and be basic layout for cars."""

if __name__ == '__main__':
    # print(url_for('static', filename='static/css/map.css'))
    # with app.test_request_context():
    #     print(url_for('static', filename='static/css/map.css'))
    app.run()
