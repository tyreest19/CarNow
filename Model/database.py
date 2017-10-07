
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
    CarID = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.VARCHAR(4))
    Model = db.Column(db.VARCHAR(50))
    Miles = db.Column(db.Integer)
    Color = db.Column(db.VARCHAR(30))

    def __repr__(self):
        return "{ " \
               "carId: '{carID}', " \
               "Year: '{Year}'"\
               "Miles: '{Miles}'"\
               "Color: '{Color}'"\
               "Model: {Model} " \
               "}".format(carID=self.carID, Brand=self.Brand, Year=self.Year, Model=self.Model,
                          Miles=self.Miles, Color=self.Color)


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