# -*- coding: UTF-8 -*-
from app import db
import datetime

class Site(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	subdomain = db.Column(db.String(20), index=True, unique=True)
	
	def __repr__(self):
		return '<Site id=%r, subdomain=%r>' % (self.id, self.subdomain)

class Location(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	site_id = db.Column(db.Integer, db.ForeignKey('site.id'))
	site = db.relationship("Site", foreign_keys=[site_id])
	suffix = db.Column(db.String(10))
	name = db.Column(db.String(20))
	description = db.Column(db.String(200))
	resorts_header = db.Column(db.String(100))
	resorts_subheader = db.Column(db.String(500))
	la = db.Column(db.String(10))
	lo = db.Column(db.String(10))

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
	how_to_get = db.Column(db.String(3000))
	url_fb_comments = db.Column(db.String(255))
	vk_id = db.Column(db.String(255))


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
	url_fb_comments = db.Column(db.String(255))
	vk_id = db.Column(db.String(255))

	def __repr__(self):
		return '<Event id=%r, dt_event=%r, resort_id=%r, name=%r>' % (
			self.id,
			self.dt_event,
			self.resort_id,
			self.name)

class News(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt_created = db.Column(db.DateTime)
	dt_news = db.Column(db.DateTime)
	resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'))
	resort = db.relationship("Resort", foreign_keys=[resort_id])
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	location = db.relationship("Location", foreign_keys=[location_id])
	name = db.Column(db.String(50))
	description = db.Column(db.String(1000))
	poster_url = db.Column(db.String(255))
	video_url = db.Column(db.String(255))
	ig_hashtag = db.Column(db.String(20))
	url_fb_comments = db.Column(db.String(255))
	vk_id = db.Column(db.String(255))

	def __repr__(self):
		return '<News id=%r, dt_news=%r, resort_id=%r, name=%r>' % (
			self.id,
			self.dt_news,
			self.resort_id,
			self.name)

class Coach(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt_created = db.Column(db.DateTime)
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	location = db.relationship("Location", foreign_keys=[location_id])
	name = db.Column(db.String(255))
	description = db.Column(db.String(1000))
	photo = db.Column(db.String(255))
	video_url = db.Column(db.String(255))
	ig_hashtag = db.Column(db.String(20))
	vk_link = db.Column(db.String(255))
	url_fb_comments = db.Column(db.String(255))
	vk_id = db.Column(db.String(255))

	def __repr__(self):
		return '<Coach id=%r, dt_created=%r, location_id=%r, name=%r>' % (
			self.id,
			self.dt_created,
			self.location_id,
			self.name)

class Cameraman(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt_created = db.Column(db.DateTime)
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	location = db.relationship("Location", foreign_keys=[location_id])
	name = db.Column(db.String(255))
	description = db.Column(db.String(1000))
	photo = db.Column(db.String(255))
	video_url = db.Column(db.String(255))
	ig_profile = db.Column(db.String(20))
	vk_profile = db.Column(db.String(255))
	fb_profile = db.Column(db.String(255))
	url_fb_comments = db.Column(db.String(255))
	vk_id = db.Column(db.String(255))

	def __repr__(self):
		return '<Cameraman id=%r, dt_created=%r, location_id=%r, name=%r>' % (
			self.id,
			self.dt_created,
			self.location_id,
			self.name)

class Rider(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt_created = db.Column(db.DateTime)
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	location = db.relationship("Location", foreign_keys=[location_id])
	name = db.Column(db.String(255))
	description = db.Column(db.String(1000))
	photo = db.Column(db.String(255))
	video_url = db.Column(db.String(255))
	ig_profile = db.Column(db.String(20))
	vk_profile = db.Column(db.String(255))
	fb_profile = db.Column(db.String(255))

	def __repr__(self):
		return '<Rider id=%r, dt_created=%r, location_id=%r, name=%r>' % (
			self.id,
			self.dt_created,
			self.location_id,
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

class Facility(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	icon = db.Column(db.String(20))
	#camps = db.relationship('Camp', secondary=camp_facilities,
	#	backref=db.backref('facilities', lazy='dynamic'))

	def __repr__(self):
		return '<Facility id=%r, name=%r, icon=%r' % (
			self.id,
			self.name,
			self.icon
			)

camp_facilities = db.Table('camp_facilities',
    db.Column('facility_id', db.Integer, db.ForeignKey('facility.id')),
    db.Column('camp_id', db.Integer, db.ForeignKey('camp.id'))
)

class Camp(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dt_create = db.Column(db.DateTime)
	dt = db.Column(db.DateTime)
	name = db.Column(db.String(100))
	description = db.Column(db.String(3000))
	url = db.Column(db.String(255))
	logo_url = db.Column(db.String(255))
	poster_url = db.Column(db.String(255))
	seats_left = db.Column(db.Integer)
	where = db.Column(db.String(255))
	is_filled = db.Column(db.Boolean)
	la = db.Column(db.String(10))
	lo = db.Column(db.String(10))
	facilities = db.relationship('Facility', secondary=camp_facilities,
		backref=db.backref('camps', lazy='dynamic'))
	slider_block = db.relationship('CampTopSliderBlock', backref='camp',
        lazy='dynamic')
	top_info_block = db.relationship('CampTopInfoBlock', backref='camp',
		lazy='dynamic')
	#top_share_block = db.relationship('CampTopShareBlock', backref='camp',
		#lazy='dynamic')
	services = db.relationship('CampServicesBlock', backref='camp',
		lazy='dynamic')
	staff = db.relationship('CampStaffBlock', backref='camp',
		lazy='dynamic')
	main_info_block = db.relationship('CampMainInfoBlock', backref='camp',
		lazy='dynamic')
	signup_form = db.relationship('CampSignUpBlock', backref='camp',
		lazy='dynamic')
	partners = db.relationship('CampPartnersBlock', backref='camp',
		lazy='dynamic')
	contact_form = db.relationship('CampContactBlock', backref='camp',
		lazy='dynamic')
	#bottom_share_block = db.relationship('CampBottomShareBlock', backref='camp',
		#lazy='dynamic')

	def __repr__(self):
		return '<Camp id=%r, name=%r, dt=%r' % (
			self.id,
			self.name,
			self.dt
		)

camp_top_slider_records = db.Table('camp_top_slider_records',
    db.Column('slider_block_id', db.Integer, db.ForeignKey('camp_top_slider_block.id')),
    db.Column('slide_record_id', db.Integer, db.ForeignKey('camp_top_slider_record.id'))
)

class CampTopSliderBlock(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'))
	slides = db.relationship('CampTopSliderRecord',
		secondary=camp_top_slider_records, 
		backref=db.backref('slider_block', lazy='dynamic')
		)
	camp_name = db.Column(db.String(20))

	def __repr__(self):
		return '<CampTopSliderBlock id=%r, camp_name=%r' % (
			self.id,
			self.camp_name
			)
	
class CampTopSliderRecord(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	index = db.Column(db.Integer)
	
	en_header = db.Column(db.String(255))
	en_subheader = db.Column(db.String(255))
	ru_header = db.Column(db.String(255))
	ru_subheader = db.Column(db.String(255))
	fr_header = db.Column(db.String(255))
	fr_subheader = db.Column(db.String(255))
	es_header = db.Column(db.String(255))
	es_subheader = db.Column(db.String(255))

	img_url_desktop = db.Column(db.String(255))
	img_url_mobile = db.Column(db.String(255))
	img_url_vertical = db.Column(db.String(255))

	def __repr__(self):
		return '<CampTopSliderRecord id=%r, header=%r' % (
			self.id,
			self.en_header
		)

class CampTopInfoBlock(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'))

	en_header = db.Column(db.String(255))
	en_subheader = db.Column(db.String(255))
	ru_header = db.Column(db.String(255))
	ru_subheader = db.Column(db.String(255))
	fr_header = db.Column(db.String(255))
	fr_subheader = db.Column(db.String(255))
	es_header = db.Column(db.String(255))
	es_subheader = db.Column(db.String(255))

	def __repr__(self):
		return '<CampTopInfoBlock id=%r, header=%r, subheader=%r' % (
			self.id,
			self.en_header,
			self.en_subheader
			)

'''class CampTopShareBlock(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'))
'''

CampServicesRecords = db.Table('camp_services_records',
    db.Column('services_block_id', db.Integer, db.ForeignKey('camp_services_block.id')),
    db.Column('service_record_id', db.Integer, db.ForeignKey('camp_service_record.id'))
)

class CampServicesBlock(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'))

	en_header = db.Column(db.String(255))
	en_subheader = db.Column(db.String(255))
	ru_header = db.Column(db.String(255))
	ru_subheader = db.Column(db.String(255))
	fr_header = db.Column(db.String(255))
	fr_subheader = db.Column(db.String(255))
	es_header = db.Column(db.String(255))
	es_subheader = db.Column(db.String(255))

	services = db.relationship('CampServiceRecord',
		secondary=CampServicesRecords, 
		backref=db.backref('services_block', lazy='dynamic')
		)

	def __repr__(self):
		return '<CampServices id=%r, header=%r, subheader=%r' % (
			self.id,
			self.en_header,
			self.en_subheader
			)

class CampServiceRecord(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	en_header = db.Column(db.String(255))
	en_subheader = db.Column(db.String(2000))
	ru_header = db.Column(db.String(255))
	ru_subheader = db.Column(db.String(2000))
	fr_header = db.Column(db.String(255))
	fr_subheader = db.Column(db.String(2000))
	es_header = db.Column(db.String(255))
	es_subheader = db.Column(db.String(2000))

	img_link = db.Column(db.String(255))

	def __repr__(self):
		return '<CampServiceRecord id=%r, header=%r, subheader=%r' % (
			self.id,
			self.en_header,
			self.en_subheader
			)

CampStaffRecords = db.Table('camp_staff_records',
    db.Column('staff_block_id', db.Integer, db.ForeignKey('camp_staff_block.id')),
    db.Column('staff_record_id', db.Integer, db.ForeignKey('camp_staff_record.id'))
)

class CampStaffBlock(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'))

	en_header = db.Column(db.String(255))
	en_subheader = db.Column(db.String(255))
	ru_header = db.Column(db.String(255))
	ru_subheader = db.Column(db.String(255))
	fr_header = db.Column(db.String(255))
	fr_subheader = db.Column(db.String(255))
	es_header = db.Column(db.String(255))
	es_subheader = db.Column(db.String(255))

	staff = db.relationship('CampStaffRecord',
		secondary=CampStaffRecords, 
		backref=db.backref('staff_block', lazy='dynamic')
		)

	def __repr__(self):
		return '<CampStaff id=%r, header=%r, subheader=%r' % (
			self.id,
			self.en_header,
			self.en_subheader
			)

class CampStaffRecord(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	order_index = db.Column(db.Integer)
	en_name = db.Column(db.String(255))
	en_role = db.Column(db.String(255))
	ru_name = db.Column(db.String(255))
	ru_role = db.Column(db.String(255))
	fr_name = db.Column(db.String(255))
	fr_role = db.Column(db.String(255))
	es_name = db.Column(db.String(255))
	es_role = db.Column(db.String(255))
	en_info = db.Column(db.String(1000))
	ru_info = db.Column(db.String(1000))
	fr_info = db.Column(db.String(1000))
	es_info = db.Column(db.String(1000))
	en_hidden = db.Column(db.String(1000))
	ru_hidden = db.Column(db.String(1000))
	fr_hidden = db.Column(db.String(1000))
	es_hidden = db.Column(db.String(1000))
	en_contacts = db.Column(db.String(1000))
	ru_contacts = db.Column(db.String(1000))
	fr_contacts = db.Column(db.String(1000))
	es_contacts = db.Column(db.String(1000))


	img_link = db.Column(db.String(255))

	def __repr__(self):
		return '<CampStaffRecord id=%r, name=%r' % (
			self.id,
			self.name
			)

CampMainInfoBlockPhotos = db.Table('camp_main_info_block_photos',
    db.Column('block_id', db.Integer, db.ForeignKey('camp_main_info_block.id')),
    db.Column('photo_id', db.Integer, db.ForeignKey('camp_main_info_block_photo.id'))
)

class CampMainInfoBlock(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'))

	en_header = db.Column(db.String(255))
	en_subheader = db.Column(db.String(255))
	ru_header = db.Column(db.String(255))
	ru_subheader = db.Column(db.String(255))
	fr_header = db.Column(db.String(255))
	fr_subheader = db.Column(db.String(255))
	es_header = db.Column(db.String(255))
	es_subheader = db.Column(db.String(255))

	en_text_header = db.Column(db.String(255))
	en_text_subheader = db.Column(db.String(255))
	ru_text_header = db.Column(db.String(255))
	ru_text_subheader = db.Column(db.String(255))
	fr_text_header = db.Column(db.String(255))
	fr_text_subheader = db.Column(db.String(255))
	es_text_header = db.Column(db.String(255))
	es_text_subheader = db.Column(db.String(255))

	en_top_text = db.Column(db.String(1000))
	en_hidden_text = db.Column(db.String(5000))
	en_bottom_text = db.Column(db.String(1000))
	ru_top_text = db.Column(db.String(1000))
	ru_hidden_text = db.Column(db.String(5000))
	ru_bottom_text = db.Column(db.String(1000))
	fr_top_text = db.Column(db.String(1000))
	fr_hidden_text = db.Column(db.String(5000))
	fr_bottom_text = db.Column(db.String(1000))
	es_top_text = db.Column(db.String(1000))
	es_hidden_text = db.Column(db.String(5000))
	es_bottom_text = db.Column(db.String(1000))

	photos = db.relationship('CampMainInfoBlockPhoto',
		secondary=CampMainInfoBlockPhotos, 
		backref=db.backref('main_info_block', lazy='dynamic')
		)

	def __repr__(self):
		return '<CampMainInfoBlock id=%r, header=%r, subheader=%r' % (
			self.id,
			self.en_header,
			self.en_subheader
			)

class CampMainInfoBlockPhoto(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	order_index = db.Column(db.Integer)
	
	en_alt = db.Column(db.String(255))
	ru_alt = db.Column(db.String(255))
	fr_alt = db.Column(db.String(255))
	es_alt = db.Column(db.String(255))

	img_link_desktop = db.Column(db.String(255))
	img_link_mobile = db.Column(db.String(255))

	def __repr__(self):
		return '<CampMainInfoBlockPhoto id=%r, alt=%r' % (
			self.id,
			self.en_alt
			)

CampSignUpOptions = db.Table('camp_sign_up_options',
	db.Column('block_id', db.Integer, db.ForeignKey('camp_sign_up_block.id')),
	db.Column('option_id', db.Integer, db.ForeignKey('camp_sign_up_option_record.id'))
)

class CampSignUpBlock(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'))

	en_header = db.Column(db.String(255))
	en_subheader = db.Column(db.String(255))
	ru_header = db.Column(db.String(255))
	ru_subheader = db.Column(db.String(255))
	fr_header = db.Column(db.String(255))
	fr_subheader = db.Column(db.String(255))
	es_header = db.Column(db.String(255))
	es_subheader = db.Column(db.String(255))

	en_form_header = db.Column(db.String(255))
	en_mailchimp_token = db.Column(db.String(20))
	ru_form_header = db.Column(db.String(255))
	ru_mailchimp_token = db.Column(db.String(20))
	fr_form_header = db.Column(db.String(255))
	fr_mailchimp_token = db.Column(db.String(20))
	es_form_header = db.Column(db.String(255))
	es_mailchimp_token = db.Column(db.String(20))

	en_signup_button = db.Column(db.String(20))
	ru_signup_button = db.Column(db.String(20))
	fr_signup_button = db.Column(db.String(20))
	es_signup_button = db.Column(db.String(20))

	currency = db.Column(db.String(10))
	initial_cost = db.Column(db.Integer)
	en_price_info = db.Column(db.String(2000))
	ru_price_info = db.Column(db.String(2000))
	fr_price_info = db.Column(db.String(2000))
	es_price_info = db.Column(db.String(2000))

	options = db.relationship('CampSignUpOptionRecord',
		secondary=CampSignUpOptions, 
		backref=db.backref('signup_block', lazy='dynamic')
		)

	def __repr__(self):
		return '<CampSignUpBlock id=%r, header=%r, subheader=%r' % (
			self.id,
			self.en_header,
			self.en_subheader
			)

class CampSignUpOptionRecord(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	order_index = db.Column(db.Integer)

	group = db.Column(db.String(20))
	value = db.Column(db.String(255))
	cost = db.Column(db.Integer)

	def __repr__(self):
		return '<CampSignUpOptionRecord id=%r, group=%r, value=%r' % (
			self.id,
			self.group,
			self.value
			)

CampPartnerRecords = db.Table('camp_partners_records',
    db.Column('block_id', db.Integer, db.ForeignKey('camp_partners_block.id')),
    db.Column('partner_id', db.Integer, db.ForeignKey('camp_partner_record.id'))
)

class CampPartnersBlock(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'))

	en_header = db.Column(db.String(255))
	en_subheader = db.Column(db.String(255))
	ru_header = db.Column(db.String(255))
	ru_subheader = db.Column(db.String(255))
	fr_header = db.Column(db.String(255))
	fr_subheader = db.Column(db.String(255))
	es_header = db.Column(db.String(255))
	es_subheader = db.Column(db.String(255))

	partners = db.relationship('CampPartnerRecord',
		secondary=CampPartnerRecords, 
		backref=db.backref('partners_block', lazy='dynamic')
		)

	def __repr__(self):
		return '<CampPartnersBlock id=%r, header=%r, subheader=%r' % (
			self.id,
			self.en_header,
			self.en_subheader
			)

class CampPartnerRecord(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	order_index = db.Column(db.Integer)

	en_name = db.Column(db.String(100))
	ru_name = db.Column(db.String(100))
	fr_name = db.Column(db.String(100))
	es_name = db.Column(db.String(100))
	
	en_description = db.Column(db.String(3000))
	ru_description = db.Column(db.String(3000))
	fr_description = db.Column(db.String(3000))
	es_description = db.Column(db.String(3000))

	url = db.Column(db.String(255))

	img_link = db.Column(db.String(255))


	def __repr__(self):
		return '<CampPertnerRecord id=%r, alt=%r' % (
			self.id,
			self.en_alt
			)

CampContactRecords = db.Table('camp_contact_records',
    db.Column('block_id', db.Integer, db.ForeignKey('camp_contact_block.id')),
    db.Column('contact_id', db.Integer, db.ForeignKey('camp_contact_record.id'))
)

CampContactUsefulPages = db.Table('camp_contact_useful_pages',
    db.Column('block_id', db.Integer, db.ForeignKey('camp_contact_block.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('camp_contact_useful_page.id'))
)

class CampContactBlock(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camp_id = db.Column(db.Integer, db.ForeignKey('camp.id'))

	email_for_letters = db.Column(db.String(255))

	en_header = db.Column(db.String(255))
	en_subheader = db.Column(db.String(255))
	en_right_subheader = db.Column(db.String(255))
	en_right_usefullpages = db.Column(db.String(255))
	ru_header = db.Column(db.String(255))
	ru_subheader = db.Column(db.String(255))
	ru_right_subheader = db.Column(db.String(255))
	ru_right_usefullpages = db.Column(db.String(255))
	fr_header = db.Column(db.String(255))
	fr_subheader = db.Column(db.String(255))
	fr_right_subheader = db.Column(db.String(255))
	fr_right_usefullpages = db.Column(db.String(255))
	es_header = db.Column(db.String(255))
	es_subheader = db.Column(db.String(255))
	es_right_subheader = db.Column(db.String(255))
	es_right_usefullpages = db.Column(db.String(255))

	contacts = db.relationship('CampContactRecord',
		secondary=CampContactRecords, 
		backref=db.backref('contact_block', lazy='dynamic')
		)

	useful_pages = db.relationship('CampContactUsefulPage',
		secondary=CampContactUsefulPages, 
		backref=db.backref('contact_block', lazy='dynamic')
		)

	def __repr__(self):
		return '<CampContactBlock id=%r, header=%r, subheader=%r' % (
			self.id,
			self.en_header,
			self.en_subheader
			)

class CampContactRecord(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	order_index = db.Column(db.Integer)

	icon_class = db.Column(db.String(20))
	link = db.Column(db.String(255))
	in_new_window = db.Column(db.Boolean)
	
	en_caption = db.Column(db.String(1000))
	ru_caption = db.Column(db.String(1000))
	fr_caption = db.Column(db.String(1000))
	es_caption = db.Column(db.String(1000))

	def __repr__(self):
		return '<CampContactRecord id=%r, caption=%r' % (
			self.id,
			self.en_caption
			)

class CampContactUsefulPage(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	order_index = db.Column(db.Integer)

	icon_class = db.Column(db.String(20))
	link = db.Column(db.String(255))
	in_new_window = db.Column(db.Boolean)

	en_caption = db.Column(db.String(1000))
	ru_caption = db.Column(db.String(1000))
	fr_caption = db.Column(db.String(1000))
	es_caption = db.Column(db.String(1000))

	def __repr__(self):
		return '<CampContactUsefulPage id=%r, caption=%r' % (
			self.id,
			self.en_caption
			)

# CampPriceOptions = db.Table('camp_price_options',
#     db.Column('block_id', db.Integer, db.ForeignKey('camp_price_block.id')),
#     db.Column('option_id', db.Integer, db.ForeignKey('camp_price_option_record.id'))
# )