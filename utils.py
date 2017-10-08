from Model import database
from twilio.rest import Client


def messageSalesRep(customer_name, customer_email, customer_message):
    print(customer_name)
    print(customer_message)
# Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC1c7bbdb77eb80d1916a3abb03c99e150"
    auth_token = "6f542f28084b112c3074ef070241e028"
    client = Client(account_sid, auth_token)
        #if customer_email == None:

    if not customer_email:
        message = client.messages.create(
        to="+13142655522",
        from_="+14159153599",
        body="Name: " + customer_name + "\n"
        + "Message: " + customer_message)

    else:
        message = client.messages.create(
        to="+13142655522",
        from_="+14159153599",
        body="Name: " + customer_name + "\n" + "Email: " + customer_email + "\n"
        + "Message: " + customer_message)


    print(message.sid)

def searchForCar(**kwargs):
    if kwargs['MODEL_YEAR'] == None:
        kwargs.pop('MODEL_YEAR')
    if kwargs['MODEL'] == None:
        kwargs.pop('MODEL')
    if kwargs['PRICE'] == None:
        kwargs.pop('PRICE')
    if kwargs['COLOR'] == 'COLOR':
        kwargs.pop('COLOR')
    return database.search(database.Car, kwargs)
