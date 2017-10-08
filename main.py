import utils
from flask import Flask, redirect,render_template, request
from Model import database
from __init__ import app


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        #utils.messageSalesRep(request.form['name'], request.form['email'], request.form['message'])
        search_results = database.search(database.Car, MODEL_YEAR=request.form['year'], MODEL=request.form['model'],
                               PRICE=request.form['price'], COLOR=request.form['color'])
        return render_template('search.html', cars=search_results)
        # redirect("/")
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
    database.create_database(app)
    app.run()

