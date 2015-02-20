from flask import Flask
from flask.ext.mobility import Mobility
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pymongo import PyMongo
from flask.ext.mongo_sessions import MongoDBSessionInterface

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
Mobility(app)
db = SQLAlchemy(app)
mongo = PyMongo(app)
with app.app_context():
    app.session_interface = MongoDBSessionInterface(app, mongo.db, 'sessions')
    
from app import views, models

if __name__ == "__main__":
    app.run(debug=True)
