from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to CarNow"


@app.route("/search")
def searchCar():
    """Page will allow users to search for a car"""



def presenetCar():
    """This page will load all the default care info and be basic layout for cars."""