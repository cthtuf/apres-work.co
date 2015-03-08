# -*- coding: UTF-8 -*-
from app import app, db, mongo
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

from pyowm import OWM,timeutils #for weather

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

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt='%d.%m.%Y'):
    return date.strftime(fmt) 

def save_location(func):
	@wraps(func)
	def wrapper(location_suffix, *args, **kwargs):
		if 'locations' not in session: session['locations'] = {}
		session['locations']['last_location_suffix'] = location_suffix
		return func(location_suffix, *args, **kwargs)
	return wrapper

@app.context_processor
def utility_processor():
    def is_menu_active(checked_page):
        if request.path == url_for(checked_page, location_suffix=session['locations']['last_location_suffix']): return 'active-menu'
    return dict(is_menu_active=is_menu_active)

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

@app.route('/')
def index():
	return redirect(url_for('location_index', location_suffix='spb'))

@app.route('/<string:location_suffix>/')
@save_location
def location_index(location_suffix):
	check_location_suffix(location_suffix)
	form = SubscriptionForm()
	return render_template('indexpage.html',
		location_suffix = location_suffix,
		form=form,
		debug=app.debug)

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


@app.route('/<string:location_suffix>/resorts/', methods=["GET"])
@save_location
def resorts(location_suffix):
	check_location_suffix(location_suffix)
	cbr = {}
	resorts = db.session.query(Resort).filter(Resort.location_id==session['locations'][location_suffix]).all()
	for resort in resorts:
		cbr[resort.id] = {
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
		location_suffix = location_suffix,
		resorts = cbr,
		rand=random.randint(1,1000000),
		debug=app.debug)

@app.route('/<string:location_suffix>/getweather/', methods=["GET"])
def getweather(location_suffix):
	result = { 'success' : 'true', 'resorts' : {} }
	try:
		check_location_suffix(location_suffix)
		#273.15
		owm = OWM(API_key=app.config['OWM_KEY'], language='ru')
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
				result['resorts'][resort.id] = {
					'current' : {
						'temp' : str(current_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
						'temp_interval' : u'от '+str(current_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C до ' +str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
						'detailed_status': current_weather.get_detailed_status(),
						'icon' : weather_icons_map[current_weather.get_weather_icon_name()],
						'wind' : {
							'speed' : current_weather.get_wind()['speed'],
							'deg' : current_weather.get_wind()['deg'],
							'speed_icon' : 'wi-beafort-'+str(int(round(current_weather.get_wind()['speed']))),
							'deg_icon' : '_'+str(round_to_base(current_weather.get_wind()['deg'], 15))+'-deg',
							'bad_deg' : resort.bad_wind_direction

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
							'deg' : in3h_weather.get_wind()['deg'],
							'speed_icon' : 'wi-beafort-'+str(int(round(in3h_weather.get_wind()['speed']))),
							'deg_icon' : '_'+str(round_to_base(in3h_weather.get_wind()['deg'], 15))+'-deg',
							'bad_deg' : resort.bad_wind_direction
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
							'deg' : in6h_weather.get_wind()['deg'],
							'speed_icon' : 'wi-beafort-'+str(int(round(in6h_weather.get_wind()['speed']))),
							'deg_icon' : '_'+str(round_to_base(in6h_weather.get_wind()['deg'], 15))+'-deg',
							'bad_deg' : resort.bad_wind_direction
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
							'deg' : in24h_weather.get_wind()['deg'],
							'speed_icon' : 'wi-beafort-'+str(int(round(in24h_weather.get_wind()['speed']))),
							'deg_icon' : '_'+str(round_to_base(in24h_weather.get_wind()['deg'], 15))+'-deg',
							'bad_deg' : resort.bad_wind_direction
						},
						'clouds' : in24h_weather.get_clouds()
					}
				}
	except Exception as e:
		print str(e)
		result = { 'success' : 'false' }
	return jsonify(result)

@app.route('/<string:location_suffix>/feedback/')
def feedback(location_suffix):
	check_location_suffix(location_suffix)
	return redirect(url_for('resorts', location_suffix=location_suffix))

@app.route('/<string:location_suffix>/howitworks/')
def howitworks(location_suffix):
	check_location_suffix(location_suffix)
	return redirect(url_for('resorts', location_suffix=location_suffix))

@app.route('/<string:location_suffix>/events/')
def events(location_suffix):
	check_location_suffix(location_suffix)

	events = Event.query.filter(Event.resort.has(location_id=session['locations'][location_suffix])).all()

	return render_template('events.html',
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		events=events,
		debug=app.debug)

@app.route('/<string:location_suffix>/news/')
@save_location
def news(location_suffix):
	check_location_suffix(location_suffix)
	return redirect(url_for('resorts', location_suffix=location_suffix))
