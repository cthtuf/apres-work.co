# -*- coding: UTF-8 -*-
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
		return '<Site id=%r, subdomain=%r>' % (self.id, self.subdomain)

class Location(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
	site = db.relationship("Site", foreign_keys=[site_id])
	suffix = db.Column(db.String(10))
	name = db.Column(db.String(20))
	description = db.Column(db.String(200))

	def __repr__(self):
		return '<Location id=%r, site_id=%r, suffix=%r, name=%r>' % (
			self.id, 
			self.site_id, 
			self.suffix,
			self.name)

class Subscription(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt = db.Column(db.DateTime)
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	location = db.relationship("Location", foreign_keys=[location_id])
	email = db.Column(db.String(120), index=True, unique=True)
	ga_client_id = db.Column(db.Integer)

	def __repr__(self):
		return '<Subscription id=%r, location_id=%r, email=%r, ga_client_id=%r>' % (
			self.id,
			self.location_id,
			self.email,
			self.ga_client_id)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt_registration = db.Column(db.DateTime)
	dt_last_action = db.Column(db.DateTime)
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	location = db.relationship("Location", foreign_keys=[location_id])
	phone = db.Column(db.String(10), index=True, unique=True)
	email = db.Column(db.String(120), index=True)
	ga_client_id = db.Column(db.Integer)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	def __init__(self, location_id, phone, email, ga_client_id):
		self.location_id = location_id
		self.dt_registration = datetime.datetime.now()
		self.phone = phone
		self.email = email
		self.ga_client_id = ga_client_id

	def __repr__(self):
		return '<User id=%r, location_id=%r, phone=%r, email=%r, ga_client_id=%r>' % (
			self.id, 
			self.location_id,
			self.phone,
			self.email,
			self.ga_client_id)

class Resorttype(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))

	def __repr__(self):
		return '<ResortType name=%r' % (self.name)

class Resort(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	type_id = db.Column(db.Integer, db.ForeignKey('resorttype.id'))
	type = db.relationship("Resorttype", foreign_keys=[type_id])
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	location = db.relationship("Location", foreign_keys=[location_id])
	name = db.Column(db.String(120))
	description = db.Column(db.String(2000))
	address = db.Column(db.String(255))
	phone = db.Column(db.String(20))
	url_site = db.Column(db.String(255))
	url_ig = db.Column(db.String(255))
	url_vk = db.Column(db.String(255))
	url_fb = db.Column(db.String(255))
	url_img = db.Column(db.String(255))
	la = db.Column(db.String(10))
	lo = db.Column(db.String(10))
	owm_id = db.Column(db.Integer)
	bad_wind_direction = db.Column(db.Integer)
	share_text = db.Column(db.String(140))

	def __repr__(self):
		return '<Resort id=%r, location_id=%r, name=%r, url_site=%r, la=%r, lo=%r, owm_id=%r>' % (
		self.id,
		self.location_id,
		self.name,
		self.url_site,
		self.la,
		self.lo,
		self.owm_id)

class Webcamera(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'))
	resort = db.relationship("Resort", foreign_keys=[resort_id])
	img_link = db.Column(db.String(255))
	iframe_link = db.Column(db.String(255))
	img_na = db.Column(db.String(255))
	load_from_iframe = db.Column(db.Boolean)

	def __repr__(self):
		return '<Webcamera id=%r, resort_id=%r, img_link=%r>' % (
			self.id,
			self.resort_id,
			self.img_link)

class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt_created = db.Column(db.DateTime)
	dt_event = db.Column(db.DateTime)
	resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'))
	resort = db.relationship("Resort", foreign_keys=[resort_id])
	name = db.Column(db.String(50))
	description = db.Column(db.String(1000))
	poster_url = db.Column(db.String(255))
	video_url = db.Column(db.String(255))
	ig_hashtag = db.Column(db.String(20))
	vk_event_url = db.Column(db.String(255))

	def __repr__(self):
		return '<Event id=%r, dt_event=%r, resort_id=%r, name=%r>' % (
			self.id,
			self.dt_event,
			self.resort_id,
			self.name)

class Partner(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'))
	resort = db.relationship("Resort", foreign_keys=[resort_id])

	def __repr__(self):
		return '<Partner id=%r, name=%r, resort_id=%r>' % (
			self.id,
			self.name,
			self.resort_id)

#id = 1 - admin
#id = 2 - moderator
#id = 3 - partner user
class StaffUser(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	email = db.Column(db.String(50))
	phone = db.Column(db.String(10))
	password = db.Column(db.String(20))
	type_id = db.Column(db.Integer)
	partner_id = db.Column(db.Integer, db.ForeignKey('partner.id'))
	partner = db.relationship("Partner", foreign_keys=[partner_id])

	def __repr__(self):
		return '<PartnerUser id=%r, name=%r, email=%r, phone=%r, password=%r>' % (
			self.id,
			self.name,
			self.email,
			self.phone,
			self.password)

class Promotion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt = db.Column(db.DateTime)
	partner_id = db.Column(db.Integer, db.ForeignKey('partner.id'))
	partner = db.relationship("Partner", foreign_keys=[partner_id])
	has_group_promocode = db.Column(db.Boolean)
	event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
	event = db.relationship("Event", foreign_keys=[event_id])

	def __repr__(self):
		return '<Promotion id=%r, dt=%r, partner_id=%r, has_group_promocode=%r, event_id=%r>' % (
			self.id,
			self.dt, 
			self.partner_id, 
			self.has_group_promocode, 
			self.event_id)

class Sms(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship("User", foreign_keys=[user_id])
	promocode_id = db.Column(db.Integer, db.ForeignKey('promocode.id'))
	promocode = db.relationship("Promocode", foreign_keys=[promocode_id])
	text = db.Column(db.String(560))

	def __repr__(self):
		return '<SMS id=%r, dt=%r, user_id=%r, promocode_id=%r, text=%r>' % (
			self.id, 
			self.dt,
			self.user_id, 
			self.promocode_id, 
			self.text)

class Promocode(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship("User", foreign_keys=[user_id])
	promotion_id = db.Column(db.Integer, db.ForeignKey('promotion.id'))
	promotion = db.relationship("Promotion", foreign_keys=[promotion_id])
	code = db.Column(db.String(10))
	is_unique = db.Column(db.Boolean)
	dt_used = db.Column(db.DateTime)

	def __repr__(self):
		return '<PromoCode id=%r, dt=%r, user_id=%r, sms_id=%r, promotion_id=%r, code=%r, is_unique=%r>' % (
			self.id,
			self.dt,
			self.user_id,
			self.sms_id,
			self.promotion_id,
			self.code,
			self.is_unique
			)