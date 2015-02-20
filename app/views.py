# -*- coding: UTF-8 -*-
from app import app, db
from functools import wraps
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from flask.ext.mobility.decorators import mobile_template
from smsc_api import SMSC
from datetime import datetime,timedelta
from .forms import SubscriptionForm
from models import *
import re
import time
import mailchimp

import string
import random
from pyowm import OWM,timeutils #for weather

weather_icons_map = {
	'01d' : 'wi-day-sunny',
	'01n' : 'wi-night-clear',
	'02d' : 'wi-day-cloudy',
	'02n' : 'wi-night-alt-cloudy',
	'03d' : 'wi-cloud',
	'03n' : 'wi-cloud',
	'04d' : 'wi-cloudy',
	'04n' : 'wi-cloudy',
	'09d' : 'wi-day-showers',
	'09n' : 'wi-night-alt-showers',
	'10d' : 'wi-day-rain',
	'10n' : 'wi-night-alt-rain',
	'11d' : 'wi-day-lightning',
	'11n' : 'wi-night-alt-lightning',
	'13d' : 'wi-snow',
	'13n' : 'wi-snow',
	'50d' : 'wi-fog',
	'50n' : 'wi-fog'
}

#def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
#	return ''.join(random.choice(chars) for _ in range(size))

#@app.before_request
#def csrf_protect():
#    if request.method in ["POST"]:
#        token = session.pop('_csrf_token', None)
#        if not token or token != request.form.get('_csrf_token'):
#            abort(403)

#def generate_csrf_token():
#    if '_csrf_token' not in session:
#        session['_csrf_token'] = string_generator(size=32)
#    return session['_csrf_token']

#app.jinja_env.globals['csrf_token'] = generate_csrf_token 

'''def valid_location(func):
	@wraps(func)
	def wrapper(location_suffix, *args, **kwargs):
		print 'decorator_1'
		if not session.has_key('location_id'):
			print 'decorator_2'
			loc = db.session.query(Location).filter_by(suffix=location_suffix)
			if loc.count()>0:
				session['location_id'] = loc.first().id
				print 'decorator_3'
			else:
				abort(404)
				print 'decorator_4'
		return func(*args, **kwargs)
	return wrapper
'''

@app.route('/')
def index():
	return redirect(url_for('location_index', location_suffix='spb'))

def check_location_suffix(location_suffix):
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


@app.route('/<string:location_suffix>/')
@mobile_template('{mobile/}index.html')
def location_index(location_suffix, template):
	check_location_suffix(location_suffix)
	form = SubscriptionForm()
	return render_template(template,
		location_suffix = location_suffix,
		form=form)

@app.route('/<string:location_suffix>/<int:event_id>/attend/', methods=["POST"])
def attend(location_suffix, event_id):
	check_location_suffix(location_suffix)
	smsc = SMSC()
	msg = 'Код для скидки: jdfsfj. Увидимся на склоне!'
	phone = re.sub("[^0-9]", "", request.form['phone'])
	print phone
	if phone[0] in ['7', '8']:
		phone = phone[1:]
	phone = '7'+phone
	print phone
	if not re.match(r"\d{10}", phone):
		return jsonify({'CODE' : '1', 'TEXT' : 'Неверный номер телефона'})
	sms_info = smsc.get_sms_cost(phone, msg)
	'''	
		sms_info[0] - sms cost
		sms_info[1] - sms count
	'''
	if float(sms_info[0]) > 3 :
		return jsonify({'CODE' : '2', 'TEXT' : 'Отправка смс на данный номер невозможна'})
	sended_sms_info = smsc.send_sms(phone, msg, sender="apresworkco")
	return jsonify({'CODE' : '0', 'TEXT' : 'Отлично! Как только наберется 8 человек мы отправим тебе смс с промо-кодом'})
	'''
		sended_sms_info[0] - sms ID
		sended_sms_info[1] - sms count
		sended_sms_info[2] - sms cost
		sended_sms_info[3] - account balance
	'''

@app.route('/<string:location_suffix>/subscribe/', methods=["POST"])
def subscribe(location_suffix):
	check_location_suffix(location_suffix)
	try:
		form = SubscriptionForm()
		if form.validate_on_submit():		
			email = form.email.data
			if not email:
				return jsonify({'CODE' : '3', 'TEXT' : 'Не указан адрес электронной почты'})
			if db.session.query(Subscription).filter_by(email=email).count()>0:
				return jsonify({'CODE' : '2', 'TEXT' : 'Вы уже подписаны'})
			subscriber = Subscription(dt=datetime.datetime.now(), location_id=session['locations'][location_suffix], email=email)
			db.session.add(subscriber)
			mc = mailchimp.Mailchimp(app.config['MAILCHIMP_TOKEN'])
			mc.lists.subscribe(app.config['MAILCHIMP_SUBSCRIPTION_LIST_ID'], {'email': email})
			db.session.commit()
			return jsonify({'CODE' : '0', 'TEXT' : 'Отлично! Чтобы подтвердить подписку, перейдите по ссылке в письме'})
		else:
			return jsonify({'CODE' : '4', 'TEXT' : 'Неверный формат Email'})	
	except mailchimp.ListAlreadySubscribedError:
		return jsonify({'CODE' : '2', 'TEXT' : 'Вы уже подписаны'})
	except mailchimp.Error, e:
		return jsonify({'CODE' : '1', 'TEXT' : 'Ошибка подписки'})


@app.route('/<string:location_suffix>/webkamery/', methods=["GET"])
def webkamery(location_suffix):#template):
	check_location_suffix(location_suffix)
	cbr = {}
	result = db.session.query(Webcamera).filter_by(location_id=session['locations'][location_suffix]).all()
	for rec in result:
		if rec.resort.id in cbr:
			cbr[rec.resort.id]['CAMERAS'].append({
				'ID' : rec.id,
				'NAME' : rec.name,
				'IMG_LINK' : rec.img_link,
				'IMG_NA' : rec.img_na
				})
		else:
			cbr[rec.resort.id] = {
				'NAME' : rec.resort.name,
				'URL_SITE' : rec.resort.url_site,
				'URL_IG' : rec.resort.url_ig,
				'URL_VK' : rec.resort.url_vk,
				'URL_FB' : rec.resort.url_fb,
				'LA' : rec.resort.la,
				'LO' : rec.resort.lo,
				'OWM_ID' : rec.resort.owm_id,
				'CAMERAS' : [{
					'ID' : rec.id,
					'NAME' : rec.name,
					'IMG_LINK' : rec.img_link,
					'IMG_NA' : rec.img_na
				}]
			}

	return render_template('webkamery.html',
		location_suffix = location_suffix,
		cbr = cbr,
		rand=random.randint(1,1000000))

@app.route('/<string:location_suffix>/gdepokatatsya/', methods=["GET"])
def gdepokatatsya(location_suffix):
	check_location_suffix(location_suffix)
	return redirect(url_for('index'))

@app.route('/getweather/', methods=["GET"])
def get_weather():
	#owm = OWM(api_key='212261a0fa0f62fe41ed0a1ba84f6627', language='ru')
	owm = OWM()
	result = {}
	#igora
	igora_obs = owm.weather_at_id(490213)
	igora_w = igora_obs.get_weather()
	next_day = datetime.now() + timedelta(days=1)
	next_3h = timeutils.next_three_hours()
	igora_f = owm.three_hours_forecast('Sosnovo')
	result['igora'] = {
		'current' : igora_w.to_JSON(),
		'forecast' : {
			'in3h' : igora_f.get_weather_at(next_3h).to_JSON(),
			'in24h' : igora_f.get_weather_at(next_day).to_JSON()
		}
	}
	return jsonify(result)