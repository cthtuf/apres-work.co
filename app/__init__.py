from flask import Flask
from flask.ext.mobility import Mobility
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pymongo import PyMongo
from flask.ext.mongo_sessions import MongoDBSessionInterface
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView
from flask.ext.babel import Babel
#from flask.ext.login import LoginManager
from flask import current_app, Blueprint, render_template
from werkzeug.debug import DebuggedApplication

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
app.debug = True
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
Mobility(app)
db = SQLAlchemy(app)
mongo = PyMongo(app)
with app.app_context():
    app.session_interface = MongoDBSessionInterface(app, mongo.db, 'sessions')

admin = Admin(app)
babel = Babel(app)

from app import urls, views, models

#admin.add_view(ModelView(models.Site, db.session))
admin.add_view(ModelView(models.Location, db.session))
#admin.add_view(ModelView(models.Subscription, db.session))
#admin.add_view(ModelView(models.User, db.session))
admin.add_view(ModelView(models.Resort, db.session))
admin.add_view(ModelView(models.Webcamera, db.session))
#admin.add_view(ModelView(models.Event, db.session))
#admin.add_view(ModelView(models.Partner, db.session))
#admin.add_view(ModelView(models.StaffUser, db.session))
#admin.add_view(ModelView(models.Promotion, db.session))
#admin.add_view(ModelView(models.Sms, db.session))
#admin.add_view(ModelView(models.Promocode, db.session))
#admin.add_view(ModelView(models.Resorttype, db.session))
admin.add_view(ModelView(models.News, db.session))
admin.add_view(ModelView(models.Coach, db.session))
admin.add_view(ModelView(models.Cameraman, db.session))
#admin.add_view(ModelView(models.Rider, db.session))
admin.add_view(ModelView(models.Camp, db.session))
admin.add_view(ModelView(models.Facility, db.session))

admin.add_view(ModelView(models.CampTopSliderBlock, db.session))
admin.add_view(ModelView(models.CampTopSliderRecord, db.session))
admin.add_view(ModelView(models.CampTopInfoBlock, db.session))
admin.add_view(ModelView(models.CampServicesBlock, db.session))
admin.add_view(ModelView(models.CampServiceRecord, db.session))
admin.add_view(ModelView(models.CampStaffBlock, db.session))
admin.add_view(ModelView(models.CampStaffRecord, db.session))
admin.add_view(ModelView(models.CampMainInfoBlock, db.session))
admin.add_view(ModelView(models.CampMainInfoBlockPhoto, db.session))
admin.add_view(ModelView(models.CampSignUpBlock, db.session))
admin.add_view(ModelView(models.CampPartnersBlock, db.session))
admin.add_view(ModelView(models.CampPartnerRecord, db.session))
admin.add_view(ModelView(models.CampContactBlock, db.session))
admin.add_view(ModelView(models.CampContactRecord, db.session))

if __name__ == "__main__":
    app.run(debug=True)
