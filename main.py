import utils
import random
from flask import Flask, redirect,render_template, request
from Model import database
from __init__ import app
from twilio.rest import Client

@app.route("/", methods=['GET'])
def home():
    print("{}".format(request.method))
    return render_template("index.html")

@app.route("/", methods=['POST'])
def process():
    search_results = database.search(database.Car, MODEL_YEAR=request.form['year'], MODEL=request.form['model'],
                                                 PRICE=request.form['price'], COLOR=request.form['color'])
    return render_template('search.html', cars=search_results)

@app.route("/map")
def parkingLot():
    # return "Map Page"
    return render_template("map.html", spot=random.randint(1, 12))

# @app.route("/sales_rep", methods=['POST'])
@app.route("/sales_rep", methods=['POST'])
def sales_rep():
    """Page will allow users to search for a car"""
    utils.messageSalesRep(request.form['name'], request.form['email'], request.form['message'])
    return redirect('/')

def presenetCar():
    """This page will load all the default care info and be basic layout for cars."""

if __name__ == '__main__':
    database.create_database(app)
    app.run(host='0.0.0.0', port='5008')