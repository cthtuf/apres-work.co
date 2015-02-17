# -*- coding: UTF-8 -*-
from app import app
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from flask.ext.mobility.decorators import mobile_template
from smsc_api import SMSC
from datetime import datetime,timedelta
from .forms import SubscriptionForm
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

@app.route('/')
@app.route('/index')
@mobile_template('{mobile/}index.html')
def index(template):
	form = SubscriptionForm()
	return render_template(template,
		form=form)

@app.route('/attend', methods=["POST"])
def attend():
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

@app.route('/subscribe', methods=["POST"])
def subscribe():
	try:
		form = SubscriptionForm()
		if form.validate_on_submit():
			mc = mailchimp.Mailchimp('c3d906f578511669ed27c60ce4079630-us10')		
			email = form.email.data
			if not email:
				return jsonify({'CODE' : '3', 'TEXT' : 'Не указан адрес электронной почты'})
			mc.lists.subscribe('55fafc9548', {'email': email})
			return jsonify({'CODE' : '0', 'TEXT' : 'Отлично! Чтобы подтвердить подписку, перейдите по ссылке в письме'})
		else:
			return jsonify({'CODE' : '4', 'TEXT' : 'Неверный формат Email'})	
	except mailchimp.ListAlreadySubscribedError:
		return jsonify({'CODE' : '2', 'TEXT' : 'Вы уже подписаны'})
	except mailchimp.Error, e:
		return jsonify({'CODE' : '1', 'TEXT' : 'Ошибка подписки'})


@app.route('/webkamery', methods=["GET"])
#@mobile_template('{mobile/}webkamery.html')
def webkamery():#template):
    return render_template('webkamery.html', rand=random.randint(1,1000000))

@app.route('/gdepokatatsya', methods=["GET"])
def gdepokatatsya():
	return redirect(url_for('index'))

@app.route('/getweather', methods=["GET"])
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
	
