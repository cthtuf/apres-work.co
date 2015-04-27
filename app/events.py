# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_loc_id, get_curr, get_path
from app import db, app
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/events/ [GET]
@cache.cached(timeout=600)
def events_g_list(language_suffix):
	save_lang(language_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		countdown_time = 'May 3, 2015 15:03:25',
		debug=app.debug)

	events = Event.query.all()

	return render_template('g_events.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		rand=random.randint(1,1000000),
		events=events,
		debug=app.debug)

#for /ru/spb/e/ [GET]
@cache.cached(timeout=600)
def events_s_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'events',
		language_suffix=language_suffix,
		location_suffix=location_suffix
	))

#for /ru/spb/events/ [GET]
@cache.cached(timeout=600)
def events_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		countdown_time = 'May 3, 2015 15:03:25',
		debug=app.debug)

	events = Event.query.filter(Event.resort.has(location_id=get_loc_id())).all()

	return render_template('l_events.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		events=events,
		debug=app.debug)

@cache.cached(timeout=600)
def events_s_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'event_page',
		language_suffix=language_suffix,
		location_suffix=location_suffix,
		id=id
	))

#for /ru/spb/event/1/ [GET]
@cache.cached(timeout=600)
def events_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	event = Event.query.filter(Event.id==id).first()

	return render_template('p_event.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		event=event,
		debug=app.debug)

#for /ru/spb/event/3/attend/ [POST]
def events_attend(language_suffix, location_suffix, event_id):
	save_lang(language_suffix)
	save_loc(location_suffix)

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