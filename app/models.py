from app import db
import datetime

class Site(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	subdomain = db.Column(db.String(20), index=True, unique=True)
	#subscriptions = db.relationship('Subscription', backref='site', lazy='dynamic')
	#users = db.relationship('User', backref='site', lazy='dynamic')
	#resorts = db.relationship('User', backref='site', lazy='dynamic')
	#events = db.relationship('User', backref='site', lazy='dynamic')
	def __repr__(self):
		return '<Site %r>' % (self.subdomain)

class Subscription(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
	site = db.relationship("Site", foreign_keys=[site_id])
	email = db.Column(db.String(120), index=True, unique=True)
	ga_client_id = db.Column(db.Integer)

	def __repr__(self):
		return '<Subscription %r>' % (self.email)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
	site = db.relationship("Site", foreign_keys=[site_id])
	phone = db.Column(db.String(10), index=True, unique=True)
	email = db.Column(db.String(120), index=True)
	ga_client_id = db.Column(db.Integer)

	def __repr__(self):
		return '<User %r, %r>' % (self.phone, self.email)

class Resort(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
	site = db.relationship("Site", foreign_keys=[site_id])
	name = db.Column(db.String(120), index=True)
	url_site = db.Column(db.String(255))
	url_ig = db.Column(db.String(255))
	url_vk = db.Column(db.String(255))
	url_fb = db.Column(db.String(255))
	la = db.Column(db.Float)
	lo = db.Column(db.Float)
	#events = db.relationship('User', backref='resort', lazy='dynamic')
	#webcameras = db.relationship('User', backref='resort', lazy='dynamic')

	def __repr__(self):
		return '<Resort %r, (%r, %r)' % (self.name, self.la, self.lo)

class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
	site = db.relationship("Site", foreign_keys=[site_id])
	dt = db.Column(db.DateTime)
	resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'))
	resort = db.relationship("Resort", foreign_keys=[resort_id])
	name = db.Column(db.String(50))
	description = db.Column(db.String(1000))

class Webcamera(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
	site = db.relationship("Site", foreign_keys=[site_id])
	resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'))
	resort = db.relationship("Resort", foreign_keys=[resort_id])
	img_link = db.Column(db.String(255))
	img_na = db.Column(db.String(255))

class SMS(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship("User", foreign_keys=[user_id])
	text = db.Column(db.String(560))

