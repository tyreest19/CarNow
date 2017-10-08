from flask import Flask, render_template, request
from Model import database
from __init__ import app


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(database.search(database.Car, MODEL_YEAR=request.form['year'], MODEL=request.form['model'],
                              PRICE=request.form['price'], COLOR=request.form['color']))
    return render_template("index.html")

@app.route("/map.html")
def parkingLot():
    return render_template("map.html")

@app.route("/search")
def searchCar():
    """Page will allow users to search for a car"""
    database.read()


@app.route("/map")
def map():
    return render_template('map.html')

def presenetCar():
    """This page will load all the default care info and be basic layout for cars."""

def messageSalesRep(customer_name, customer_message):
    print(customer_name)
    print(customer_message)

if __name__ == '__main__':
    database.create_database(app)
    app.run()

