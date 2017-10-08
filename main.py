from flask import Flask, render_template, request
from Model import database
from twilio.rest import Client

app = Flask(__name__, template_folder='View/templates/', static_folder='View')
app.config['DEBUG'] = False

def messageSalesRep(customer_name, customer_message):
    print(customer_name)
    print(customer_message)
# Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC1c7bbdb77eb80d1916a3abb03c99e150"
    auth_token = "6f542f28084b112c3074ef070241e028"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+13142655522",
        from_="+14159153599",
        body=customer_name + ": " + customer_message)
    print(message.sid)

@app.route("/", methods=['GET', 'POST'])
def home():

    messageSalesRep("Miles","hi")
    # return "Welcome to CarNow"
    if request.method == 'POST':
        messageSalesRep(request.form['name'], request.form['message'])
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



if __name__ == '__main__':
    # print(url_for('static', filename='static/css/map.css'))
    # with app.test_request_context():
    #     print(url_for('static', filename='static/css/map.css'))
    app.run()
