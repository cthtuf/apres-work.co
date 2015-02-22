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
	result = db.session.query(Resort, Webcamera).join(Webcamera).filter(Resort.location_id==session['locations'][location_suffix]).all()
	#print str(result)
	#for rec in result:
	#	print str(rec)
	#	print ''
	#return ''
	#result = db.session.query(Webcamera).filter_by(resort.location_id=session['locations'][location_suffix]).all()
	for rec in result:
		if rec.Resort.id in cbr:
			cbr[rec.Resort.id]['CAMERAS'].append({
				'ID' : rec.Webcamera.id,
				'NAME' : rec.Webcamera.name,
				'IMG_LINK' : rec.Webcamera.img_link,
				'IMG_NA' : rec.Webcamera.img_na
				})
		else:
			cbr[rec.Resort.id] = {
				'NAME' : rec.Resort.name,
				'URL_SITE' : rec.Resort.url_site,
				'URL_IG' : rec.Resort.url_ig,
				'URL_VK' : rec.Resort.url_vk,
				'URL_FB' : rec.Resort.url_fb,
				'LA' : rec.Resort.la,
				'LO' : rec.Resort.lo,
				'OWM_ID' : rec.Resort.owm_id,
				'CAMERAS' : [{
					'ID' : rec.Webcamera.id,
					'NAME' : rec.Webcamera.name,
					'IMG_LINK' : rec.Webcamera.img_link,
					'IMG_NA' : rec.Webcamera.img_na
				}]
			}

	return render_template('webkamery.html',
		location_suffix = location_suffix,
		cbr = cbr,
		rand=random.randint(1,1000000))

@app.route('/<string:location_suffix>/sobytiya/', methods=["GET"])
def sobytiya(location_suffix):
	check_location_suffix(location_suffix)
	return render_template('sobytiya.html',
		location_suffix=location_suffix,
		active_event = active_events,
		past_events = past_events
		)

@app.route('/<string:location_suffix>/gdepokatatsya/', methods=["GET"])
def gdepokatatsya(location_suffix):
	check_location_suffix(location_suffix)
	return redirect(url_for('index'))

@app.route('/<string:location_suffix>/getweather/', methods=["GET"])
def get_weather(location_suffix):
	check_location_suffix(location_suffix)
	#273.15
	owm = OWM(API_key=app.config['OWM_KEY'], language='ru')
	result = {}
	resorts = db.session.query(Resort).filter_by(location_id=session['locations'][location_suffix]).all()
	if len(resorts)>0:
		for resort in resorts:
			if not resort.owm_id: continue
			observation = owm.weather_at_id(resort.owm_id)
			current_weather = observation.get_weather()
			next_day = datetime.datetime.now() + timedelta(days=1)
			next_3h = datetime.datetime.now() + timedelta(hours=3)
			next_6h = datetime.datetime.now() + timedelta(hours=6)
			forecast_weather = owm.three_hours_forecast_at_id(resort.owm_id)
			in3h_weather = forecast_weather.get_weather_at(next_3h)
			in6h_weather = forecast_weather.get_weather_at(next_6h)
			in24h_weather = forecast_weather.get_weather_at(next_day)
			#print str(current_weather)
			#print 
			result[resort.id] = {
				'current' : {
					'temp' : str(current_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
					'temp_interval' : u'от '+str(current_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C до ' +str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
					'detailed_status': current_weather.get_detailed_status(),
					'icon' : weather_icons_map[current_weather.get_weather_icon_name()],
					'wind' : {
						'speed' : current_weather.get_wind()['speed'],
						'deg' : current_weather.get_wind()['deg']
					},
					'clouds' : current_weather.get_clouds()
				},
				'in3h' : {
					'temp' : str(in3h_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
					'temp-interval' : u'от '+str(in3h_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C до ' +str(in3h_weather.get_temperature(unit='celsius')['temp_max']) + u'\u00B0C', 
					'detailed_status': in3h_weather.get_detailed_status(),
					'icon' : weather_icons_map[in3h_weather.get_weather_icon_name()],
					'wind' : {
						'speed' : in3h_weather.get_wind()['speed'],
						'deg' : in3h_weather.get_wind()['deg']
					},
					'clouds' : in3h_weather.get_clouds()
				},
				'in6h' : {
					'temp' : str(in6h_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
					'temp-interval' : u'от '+str(in6h_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C до ' +str(in6h_weather.get_temperature(unit='celsius')['temp_max']) + u'\u00B0C', 
					'detailed_status': in6h_weather.get_detailed_status(),
					'icon' : weather_icons_map[in6h_weather.get_weather_icon_name()],
					'wind' : {
						'speed' : in6h_weather.get_wind()['speed'],
						'deg' : in6h_weather.get_wind()['deg']
					},
					'clouds' : in6h_weather.get_clouds()
				},
				'in24h' : {
					'temp' : str(in24h_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
					'temp-interval' : u'от '+str(in24h_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C до ' +str(in24h_weather.get_temperature(unit='celsius')['temp_max']) + u'\u00B0C', 
					'detailed_status': in24h_weather.get_detailed_status(),
					'icon' : weather_icons_map[in24h_weather.get_weather_icon_name()],
					'wind' : {
						'speed' : in24h_weather.get_wind()['speed'],
						'deg' : in24h_weather.get_wind()['deg']
					},
					'clouds' : in24h_weather.get_clouds()
				}
			}
	return jsonify(result)