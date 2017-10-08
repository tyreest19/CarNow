from flask import Flask

app = Flask(__name__, template_folder='View/templates/', static_folder='View')
app.config['DEBUG'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql3198257:fTL6wulZHf@sql3.freemysqlhosting.net/sql3198257'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
