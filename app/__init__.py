from flask import Flask
from flask.ext.mobility import Mobility
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
Mobility(app)
db = SQLAlchemy(app)
from app import views, models

app.secret_key = 'fsd98UI@JHDSA^%!&*(DSOIAUHBCNXZ289eda78uih2ed*(SA'

if __name__ == "__main__":
    app.run(debug=True)
