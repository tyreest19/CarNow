import utils
import random
from flask import Flask, redirect,render_template, request
from Model import database
from __init__ import app
from twilio.rest import Client


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if None not in (request.form['name'], request.form['email'], request.form['message']):
            utils.messageSalesRep(request.form['name'], request.form['email'], request.form['message'])
        search_results = database.search(database.Car, MODEL_YEAR=request.form['year'], MODEL=request.form['model'],
                                             PRICE=request.form['price'], COLOR=request.form['color'])
        return render_template('search.html', cars=search_results)
    return render_template("index.html")

@app.route("/map.html")
def parkingLot():
    # return "Map Page"

    return render_template("map.html", spot=random.randint(1, 12))


@app.route("/sales_rep", methods=['GET', 'POST'])
def sales_rep():
    """Page will allow users to search for a car"""
    return redirect('/')

def presenetCar():
    """This page will load all the default care info and be basic layout for cars."""

# @app.route("/", methods=['POST'])
# def messageSalesRep():
#     from twilio.rest import Client
#     customer_name = request.form['name']
#     customer_email = request.form['email']
#     customer_message = request.form['message']
#     print(customer_name)
#     print(customer_message)
# # Your Account Sid and Auth Token from twilio.com/user/account
#     account_sid = "AC1c7bbdb77eb80d1916a3abb03c99e150"
#     auth_token = "6f542f28084b112c3074ef070241e028"
#     client = Client(account_sid, auth_token)
#         #if customer_email == None:
#
#     if not customer_email:
#         message = client.messages.create(
#         to="+13142655522",
#         from_="+14159153599",
#         body="Name: " + customer_name + "\n"
#         + "Message: " + customer_message)
#
#     else:
#         message = client.messages.create(
#         to="+13142655522",
#         from_="+14159153599",
#         body="Name: " + customer_name + "\n" + "Email: " + customer_email + "\n"
#         + "Message: " + customer_message)
#
#
#     print(message.sid)

if __name__ == '__main__':
    database.create_database(app)
    app.run()

