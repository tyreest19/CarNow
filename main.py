from flask import Flask, render_template
from Model import database
app = Flask(__name__, template_folder='View/templates/', static_folder='View')
app.config['DEBUG'] = False


@app.route("/")
def home():
    # return "Welcome to CarNow"
    return render_template("index.html")


@app.route("/search")
def searchCar():
    """Page will allow users to search for a car"""
    database.read()


@app.route("/map")
def map():
    return render_template('map.html')

def presenetCar():
    """This page will load all the default care info and be basic layout for cars."""

if __name__ == '__main__':
    app.run()