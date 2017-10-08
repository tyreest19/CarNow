from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql3198257:fTL6wulZHf@sql3.freemysqlhosting.net/sql3198257'
db = SQLAlchemy(app)

def init_app(app):
    # Disable track modifications, as it unnecessarily uses memory.
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)


def from_sql(row):
    """Translates a SQLAlchemy model instance into a dictionary"""
    data = row.__dict__.copy()
    return data

class Car(db.Model):
    """This class represents the Car table."""
    __tablename__ = "Car"
    CAR_ID = db.Column(db.Integer, primary_key=True)
    DEALER_NUMBER = db.Column(db.Integer)
    MODEL_YEAR = db.Column(db.VARCHAR(4))
    MODEL_NUMBER = db.Column(db.VARCHAR(50))
    MODEL = db.Column(db.VARCHAR(50))
    DESCRIPTION = db.Column(db.VARCHAR(50))
    DRIVETRAIN_NAME = db.Column(db.VARCHAR(10))
    STOCK_QTY = db.Column(db.Integer)
    MILEAGE = db.Column(db.Integer)
    COLOR = db.Column(db.VARCHAR(20))

    def __repr__(self):
        return "{ " \
               "CAR_ID: {CAR_ID}, " \
               "YEAR: {YEAR}"\
               "MILEAGE: {MILEAGE}"\
               "COLOR: {COLOR}"\
               "MODEL_NUMBER: {MODEL_NUMBER} " \
               "TOMS_SERIES_NAME: {TOMS_SERIES_NAME}"\
               "DESCRIPTION: {DESCRIPTION}"\
               "STOCK_QTY: {STOCK_QTY}"\
               "}".format(CAR_ID=self.CAR_ID, DESCRIPTION=self.DESCRIPTION, YEAR=self.YEAR, MODEL=self.MODEL,
                          MILEAGE=self.MILEAGE, COLOR=self.COLOR, MODEL_NUMBER=self.MODEL_NUMBER,
                          DRIVETRAIN_NAME=self.DRIVETRAIN_NAME, DEALER_NUMBER=self.DEALER_NUMBER,
                          STOCK_QTY=self.STOCK_QTY)


class CarKey(db.Model):
    """This class represents the Key table"""
    __tablename__ = "CarKey"
    KeyID = db.Column(db.Integer, primary_key=True)
    CarID = db.Column(db.Integer, db.ForeignKey('Car.CarID'), nullable=False)


    def __repr__(self):
        return "{ " \
               "KeyID: '{KeyID}', " \
               "CarID: '{CarID}"\
               "}".format(KeyID=self.KeyID, CarID=self.CarID)

class SalesPerson(db.Model):
    """This class represents the SalesPerson table"""
    __tablename__ = "SalesPerson"
    SalesPersonID = db.Column(db.Integer, primary_key=True)
    FName = db.Column(db.VARCHAR(30))
    LName = db.Column(db.VARCHAR(30))


    def __repr__(self):
        return "{ " \
               "FName: '{FName}', " \
               "LName: '{LName}"\
               "}".format(FName=self.FName, LName=self.LName)

def read(table, id):
    """Reads a row from desried table within the SaveMeTime database
        Arguements:
            table: Pass in the reference to the desired table object above.
            id: Id for desired row.
        Returns:
            A dictionary containing containing the rows information.
    """
    result = table.query.get(id)
    if not result:
        return None
    return from_sql(result)
# [END read]


# [START create]
def create(table, data):
    """Adds row to a table.
        Arguements:
            table: Pass in the reference to the desired table object above.
            data: Pass in dictionary containing the values for the row.
        Returns:
            A dictionary containing containing the rows information.
    """
    row = table(**data)
    db.session.add(row)
    db.session.commit()
    return from_sql(row)
# [END create]


# [START update]
def update(table, id, data):
    """Updates a table\'s row.
        Arguements:
            table: Pass in the reference to the desired table object above.
            id: Id for desired row.
            data: Pass in dictionary containing the values for the row.
        Returns:
            A dictionary containing containing the rows information.
    """
    row = table.query.get(id)
    for k, v in data.items():
        setattr(row, k, v)
    db.session.commit()
    return from_sql(row)
