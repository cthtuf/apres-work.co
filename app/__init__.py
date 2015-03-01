from flask import Flask
from flask.ext.mobility import Mobility
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pymongo import PyMongo
from flask.ext.mongo_sessions import MongoDBSessionInterface
#from flask.ext.admin import Admin
#from flask.ext.admin.contrib.sqlamodel import ModelView
#from flask.ext.login import LoginManager

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
Mobility(app)
db = SQLAlchemy(app)
mongo = PyMongo(app)
with app.app_context():
    app.session_interface = MongoDBSessionInterface(app, mongo.db, 'sessions')

#admin = Admin(app)

from app import views, models
'''
admin.add_view(ModelView(models.Site, db.session))
admin.add_view(ModelView(models.Location, db.session))
admin.add_view(ModelView(models.Subscription, db.session))
admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Resort, db.session))
admin.add_view(ModelView(models.Webcamera, db.session))
admin.add_view(ModelView(models.Event, db.session))
admin.add_view(ModelView(models.Partner, db.session))
admin.add_view(ModelView(models.StaffUser, db.session))
admin.add_view(ModelView(models.Promotion, db.session))
admin.add_view(ModelView(models.Sms, db.session))
admin.add_view(ModelView(models.Promocode, db.session))
'''
app.debug = True
if __name__ == "__main__":
    app.run(debug=True)
