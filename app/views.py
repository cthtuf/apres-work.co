# -*- coding: UTF-8 -*-
from app import app, db, mongo, babel
from functools import wraps
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from flask.ext.login import LoginManager, UserMixin, login_required
from flask.ext.mobility.decorators import mobile_template
from smsc_api import SMSC
from datetime import datetime,timedelta
from .forms import SubscriptionForm
from models import *
from helpers import *
import re
import time
import mailchimp
import flask.ext.admin
import urllib
import sys
from flask.ext.babel import gettext
from pprint import pprint

@babel.localeselector
def get_locale(language_suffix=''):
	if language_suffix != '' and language_suffix in app.config['LANGUAGES'].keys():
		return language_suffix
	elif hasattr(request, 'language_suffix'):
		return request.language_suffix
	else:
		return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

def get_site_url():
	return u'http://apres-work.co' #to-do add support of subdomains

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt='%d.%m.%Y'):
    return date.strftime(fmt) 

def save_suffixes(func):
	@wraps(func)
	def wrapper(language_suffix, location_suffix, *args, **kwargs):
		request.language_suffix = language_suffix
		request.location_suffix = location_suffix
		#session['last_language_suffix'] = language_suffix
		#session['last_location_suffix'] = location_suffix
		return func(language_suffix, location_suffix, *args, **kwargs)
	return wrapper

@app.context_processor
def utility_processor():
    def is_menu_active(checked_page):
        if request.path == url_for(
        	checked_page,
        	location_suffix=request.location_suffix, #  session['last_location_suffix'],
        	language_suffix=request.language_suffix # session['last_language_suffix']
        	): return 'active-menu'
    return dict(is_menu_active=is_menu_active)

@app.context_processor
def utility_processor():
	def get_img_src(path, filename_desktop, filename_mobile):
		if request.MOBILE:
			return url_for('static', filename=path+filename_mobile)
		else:
			return url_for('static', filename=path+filename_desktop)
	return dict(get_img_src=get_img_src)

def check_suffixes(language_suffix, location_suffix):
	if not session.has_key('locations') or not session['locations'].has_key(location_suffix):
		loc = db.session.query(Location).filter_by(suffix=location_suffix)
		if loc.count()>0:
			if not session.has_key('locations'):
				session['locations'] = {}
			session['locations'][location_suffix] = loc.first().id
			return True
		else:
			abort(404)
	else:
		return True

# for / [GET]
def index():
	return redirect(url_for(
		'camp',
		language_suffix='en',#get_locale(),
		location_suffix='l2a' #get_location()
	))

# for /ru/ [GET]
def language_index(language_suffix):
	return redirect(url_for(
		'camp',
		language_suffix='en',
		location_suffix='l2a'
	))

#for /ru/spb/ [GET]
@save_suffixes
def location_index(language_suffix, location_suffix):
	check_suffixes(language_suffix, location_suffix)
	form = SubscriptionForm()
	return render_template('indexpage.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		form=form,
		debug=app.debug)

#for /ru/spb/3/attend/ [POST]
@save_suffixes
def event_attend(language_suffix, location_suffix, event_id):
	check_suffixes(language_suffix, location_suffix)
	smsc = SMSC()
	msg = gettext("Your promocode: _code_. See you!").replace('_code_', '123123')
	phone = re.sub("[^0-9]", "", request.form['phone'])
	print phone
	if phone[0] in ['7', '8']:
		phone = phone[1:]
	phone = '7'+phone
	print phone
	if not re.match(r"\d{10}", phone):
		return jsonify({'CODE' : '1', 'TEXT' : gettext("Incorrect format")})
	sms_info = smsc.get_sms_cost(phone, msg)
	'''	
		sms_info[0] - sms cost
		sms_info[1] - sms count
	'''
	if float(sms_info[0]) > 3 :
		return jsonify({'CODE' : '2', 'TEXT' : gettext("We can't send the sms to this number")})
	sended_sms_info = smsc.send_sms(phone, msg, sender="apresworkco")
	return jsonify({
		'CODE' : '0',
		'TEXT' : gettext("Great! When the count of people will be enough, we will send promo-code to you in sms.")
	})
	'''
		sended_sms_info[0] - sms ID
		sended_sms_info[1] - sms count
		sended_sms_info[2] - sms cost
		sended_sms_info[3] - account balance
	'''

# /ru/spb/subscribe/ [POST]
@save_suffixes
def subscribe(language_suffix, location_suffix):
	check_suffixes(language_suffix, location_suffix)
	try:
		form = SubscriptionForm()
		if form.validate_on_submit():		
			email = form.email.data
			if not email:
				return jsonify({'CODE' : '3', 'TEXT' : gettext('Set email address, please')})
			if db.session.query(Subscription).filter_by(email=email).count()>0:
				return jsonify({'CODE' : '2', 'TEXT' : gettext("You're already subscribed. Thank you!")})
			subscriber = Subscription(dt=datetime.datetime.now(), location_id=session['locations'][location_suffix], email=email)
			db.session.add(subscriber)
			mc = mailchimp.Mailchimp(app.config['MAILCHIMP_TOKEN'])
			mc.lists.subscribe(app.config['MAILCHIMP_SUBSCRIPTION_LIST_ID'], {'email': email, 'double_optin' : false, 'send_welcome' : true})
			db.session.commit()
			return jsonify({
				'CODE' : '0',
				'TEXT' : gettext("Great! You're sucessfully subscribed.")
			})
		else:
			return jsonify({'CODE' : '4', 'TEXT' : gettext("Incorrect format of the Email")})	
	except mailchimp.ListAlreadySubscribedError:
		return jsonify({'CODE' : '2', 'TEXT' : gettext("You're already subscribed. Thank you!")})
	except mailchimp.Error, e:
		return jsonify({'CODE' : '1', 'TEXT' : gettext("An error occured. Please repeat.")})

# /ru/spb/r/ [GET]
@save_suffixes
def resorts_short(language_suffix, location_suffix):
	check_suffixes(language_suffix, location_suffix)
	return redirect(url_for(
		'resorts',
		language_suffix=language_suffix,
		location_suffix=location_suffix
	))

# /ru/spb/resorts/ [GET]
@save_suffixes
def resorts(language_suffix, location_suffix):
	'''
	if location_suffix == 'l2a':
		location_header = 'Les Deux Alpes'.encode('utf-8')
		location_subheader = "Les Deux Alpes is one of those resorts where you can initially struggle to discover just why it's so popular with British skiers.".encode('utf-8')
	elif location_suffix == 'spb':
		location_header = 'Парки Санкт-Петербурга и Ленинградской области'.encode('utf-8')
		location_subheader = 'На странице предоставлены только те горнолыжные центры, в которых присутствуют экстрим-парки.'.encode('utf-8')
	elif location_suffix == 'msk':
		location_header = 'Парки Москвы и Московской области'.encode('utf-8')
		location_subheader = 'На странице предоставлены только те горнолыжные центры, в которых присутствуют экстрим-парки.'.encode('utf-8')
	'''
	check_suffixes(language_suffix, location_suffix)
	cbr = {}
	resorts = db.session.query(Resort).filter(Resort.location_id==session['locations'][location_suffix]).all()
	location = db.session.query(Location).filter(Location.suffix==location_suffix).first()
	for resort in resorts:
		share_text = resort.share_text.replace('_url_', get_site_url()+url_for('resorts_short', language_suffix=language_suffix, location_suffix=location_suffix)+'#id'+str(resort.id))
		share_text = share_text.encode('utf-8')
		#share_text = share_text+'#'+resort.name)
		#print share_text
		share_text = urllib.quote(share_text)
		#print share_text
		cbr[resort.id] = {
			'ID' : resort.id,
			'NAME' : resort.name,
			'PHONE' : resort.phone,
			'ADDRESS' : resort.address,
			'URL_SITE' : resort.url_site,
			'URL_IG' : resort.url_ig,
			'URL_VK' : resort.url_vk,
			'URL_FB' : resort.url_fb,
			'URL_IMG': resort.url_img,
			'LA' : resort.la,
			'LO' : resort.lo,
			'OWM_ID' : resort.owm_id,
			'DESCRIPTION' : resort.description,
			'SHARE_TEXT' : share_text,
			'CAMERAS' : []
		}
	webcameras = db.session.query(Resort, Webcamera).join(Webcamera).filter(Resort.location_id==session['locations'][location_suffix]).all()
	for camera in webcameras:
		cbr[camera.Resort.id]['CAMERAS'].append({
				'ID' : camera.Webcamera.id,
				'NAME' : camera.Webcamera.name,
				'IMG_LINK' : camera.Webcamera.img_link,
				'IFRAME_LINK' : camera.Webcamera.iframe_link,
				'IMG_NA' : camera.Webcamera.img_na,
				'LOAD_FROM_IFRAME' : camera.Webcamera.load_from_iframe
			})
	return render_template('resorts.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		resorts = cbr,
		location_header = location.resorts_header,
		location_subheader = location.resorts_subheader,
		rand=random.randint(1,1000000),
		debug=app.debug)

# /ru/spb/feedback/ [GET]
@save_suffixes
def feedback(language_suffix, location_suffix):
	check_suffixes(language_suffix, location_suffix)
	return redirect(url_for(
		'resorts',
		language_suffix = language_suffix,
		location_suffix=location_suffix
	))

# /ru/spb/howitworks/ [GET]
@save_suffixes
def howitworks(language_suffix, location_suffix):
	check_suffixes(language_suffix, location_suffix)
	return redirect(url_for(
		'resorts',
		language_suffix=language_suffix,
		location_suffix=location_suffix
	))

# /ru/spb/e/ [GET]
@save_suffixes
def events_short(language_suffix, location_suffix):
	check_suffixes(language_suffix, location_suffix)
	return redirect(url_for(
		'events',
		language_suffix=language_suffix,
		location_suffix=location_suffix
	))

# /ru/spb/events/ [GET]
@save_suffixes
def events(language_suffix, location_suffix):
	check_suffixes(language_suffix, location_suffix)

	events = Event.query.filter(Event.resort.has(location_id=session['locations'][location_suffix])).all()

	return render_template('events.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		events=events,
		debug=app.debug)

# /ru/spb/news/ [GET]
@save_suffixes
def news(language_suffix, location_suffix):
	check_suffixes(language_suffix, location_suffix)
	return redirect(url_for(
		'resorts',
		language_suffix = language_suffix,
		location_suffix=location_suffix
	))

def get_camp_list_id(language_suffix):
	if language_suffix == 'ru':
		return app.config['MAILCHIMP_CAMP_L2A15_RU']
	elif language_suffix == 'fr':
		return app.config['MAILCHIMP_CAMP_L2A15_FR']
	else:
		return app.config['MAILCHIMP_CAMP_L2A15_EN']

# /__lang__/__loc__/camp/ [GET]
@save_suffixes
def camp(language_suffix, location_suffix):
	mailchimp_list_token = get_camp_list_id(language_suffix)
	mc = mailchimp.Mailchimp(app.config['MAILCHIMP_TOKEN'])
	mailchimp_form = {}
	try:
		mailchimp_form = mc.lists.merge_vars({'id' : mailchimp_list_token})
		mailchimp_form = mailchimp_form['data'][0]['merge_vars']
	except Exception, e:
		print e
	return render_template(
		'camp.html',
		language_suffix = language_suffix,
		location_suffix = 'l2a',
		debug=app.debug,
		mailchimp_form=mailchimp_form
	)

# /__lang__/__loc__/camp/ [POST]
@save_suffixes
def camp_attend(language_suffix, location_suffix):
	mailchimp_list_token = get_camp_list_id(language_suffix)
	mc = mailchimp.Mailchimp(app.config['MAILCHIMP_TOKEN'])
	merge_fields = {}
	for k,v in request.form.iteritems():
		if k != 'EMAIL':
			merge_fields[k] = v

	try:
		mc.lists.subscribe(
			mailchimp_list_token,
			{ 'email': request.form['EMAIL']}, 
			merge_fields,
			double_optin=False,
			send_welcome=True,
			update_existing=True
		)

		return jsonify({'CODE' : '0', 'TEXT' : gettext("You're in! We'll call you soon to confirm details")})

	except mailchimp.ListAlreadySubscribedError:
		return jsonify({'CODE' : '2', 'TEXT' : gettext("You're already subscribed. Thank you!")})
	except mailchimp.Error, e:
		return jsonify({'CODE' : '1', 'TEXT' : gettext("An error occured. Please repeat.")})