
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    # Disable track modifications, as it unnecessarily uses memory.
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)


def from_sql(row):
    """Translates a SQLAlchemy model instance into a dictionary"""
    data = row.__dict__.copy()
    data['id'] = row.id
    data.pop('_sa_instance_state')
    return data

class Car(db.Model):
    """This class represents the User table."""
    __tablename__ = "User"
    carID = db.Column(db.Integer, primary_key=True)
    Brand = db.Column(db.VARCHAR(30))
    Year = db.Column(db.VARCHAR(4))
    Model = db.Column(db.VARCHAR(50))
    Miles = db.Column(db.Integer)
    Color = db.Column(db.VARCHAR(30))

    def __repr__(self):
        return "{ " \
               "carId: '{carID}', " \
               "Brand: '{Brand}"\
               "Year: '{Year}'"\
               "Miles: '{Miles}'"\
               "Color: '{Color}'"\
               "Model: {Model} " \
               "}".format(carID=self.carID, Brand=self.Brand, Year=self.Year, Model=self.Model,
                          Miles=self.Miles, Color=self.Color)


class Key(db.Model):
    """This class represents the DailyActivity table"""
    __tablename__ = "DailyActivity"
    KeyID = db.Column(db.Integer, primary_key=True)
    CarID = db.Column(db.Integer, db.ForeignKey('Car.CarID'), nullable=False)


    def __repr__(self):
        return "{ " \
               "KeyID: '{KeyID}', " \
               "CarID: '{CarID}"\
               "}".format(KeyID=self.KeyID, CarID=self.CarID)

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
def update(data, id, table):
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

def _create_database():
    """
    If this script is run directly, create all the tables necessary to run the
    application.
    """
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    init_app(app)
    with app.app_context():
        db.create_all()
    print("All tables created")


if __name__ == '__main__':
    _create_database()