# -*- coding: utf-8 -*-
from pyowm import OWM,timeutils #for weather
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_loc_id, get_curr
from app import db, app
from models import *
from flask import request, jsonify, session
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

def getweather(location_suffix):
	result = { 'success' : 'true', 'resorts' : {} }
	#try:
	if True:
		location_suffix = save_loc(location_suffix)
		#API_key=app.config['OWM_KEY'], 
		owm = OWM(config_module='pyowm_config', language='ru')
		resorts = db.session.query(Resort).filter_by(location_id=get_loc_id()).all()
		if len(resorts)>0:
			for resort in resorts:
				if not resort.owm_id: continue
				observation = owm.weather_at_id(resort.owm_id)

				current_hour = datetime.now().hour

				today_night = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 3, 0, 0)
				today_morning = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9, 0, 0)
				today_day = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 14, 0, 0)
				today_evening = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 19, 0, 0)
				tomorrow_night = today_night + timedelta(days=1)
				tomorrow_morning = today_morning + timedelta(days=1)
				tomorrow_day = today_day + timedelta(days=1)
				tomorrow_evening = today_evening + timedelta(days=1)

				#next_day = datetime.now() + timedelta(days=1)
				#next_3h = datetime.now() + timedelta(hours=3)
				#next_6h = datetime.now() + timedelta(hours=6)
				current_weather = observation.get_weather()
				forecast_weather = owm.three_hours_forecast_at_id(resort.owm_id)
				#in3h_weather = forecast_weather.get_weather_at(next_3h)
				#in6h_weather = forecast_weather.get_weather_at(next_6h)
				#in24h_weather = forecast_weather.get_weather_at(next_day)
				today_night_weather = forecast_weather.get_weather_at(today_night) if current_hour < 4 else False
				today_morning_weather = forecast_weather.get_weather_at(today_morning) if current_hour < 10 else False
				today_day_weather = forecast_weather.get_weather_at(today_day) if current_hour < 15 else False
				today_evening_weather = forecast_weather.get_weather_at(today_evening) if current_hour < 20 else False
				tomorrow_night_weather = forecast_weather.get_weather_at(tomorrow_night)
				tomorrow_morning_weather = forecast_weather.get_weather_at(tomorrow_morning)
				tomorrow_day_weather = forecast_weather.get_weather_at(tomorrow_day)
				tomorrow_evening_weather = forecast_weather.get_weather_at(tomorrow_evening) 
				#print str(current_weather)
				#print 
				current_weather_object = {
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
				}
				if today_night_weather:
					today_night_weather_object = {
						'temp' : str(today_night_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
						'temp_interval' : u'от '+str(today_night_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C до ' +str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
						'detailed_status': today_night_weather.get_detailed_status(),
						'icon' : weather_icons_map[today_night_weather.get_weather_icon_name()],
						'wind' : {
							'speed' : today_night_weather.get_wind()['speed'],
							'deg' : today_night_weather.get_wind()['deg'],
							'speed_icon' : 'wi-beafort-'+str(int(round(today_night_weather.get_wind()['speed']))),
							'deg_icon' : '_'+str(round_to_base(today_night_weather.get_wind()['deg'], 15))+'-deg',
							'bad_deg' : resort.bad_wind_direction

						},
						'clouds' : today_night_weather.get_clouds()
					}
				else: today_night_weather_object = {}

				if today_night_weather:
					today_night_weather_object = {
						'temp' : str(today_night_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
						'temp_interval' : u'от '+str(today_night_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C до ' +str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
						'detailed_status': today_night_weather.get_detailed_status(),
						'icon' : weather_icons_map[today_night_weather.get_weather_icon_name()],
						'wind' : {
							'speed' : today_night_weather.get_wind()['speed'],
							'deg' : today_night_weather.get_wind()['deg'],
							'speed_icon' : 'wi-beafort-'+str(int(round(today_night_weather.get_wind()['speed']))),
							'deg_icon' : '_'+str(round_to_base(today_night_weather.get_wind()['deg'], 15))+'-deg',
							'bad_deg' : resort.bad_wind_direction

						},
						'clouds' : today_night_weather.get_clouds()
					}
				else: today_night_weather_object = {}

				if today_morning_weather:
					today_morning_weather_object = {
						'temp' : str(today_morning_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
						'temp_interval' : gettext('from')+' '+str(today_morning_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C '+gettext('to')+' '+str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
						'detailed_status': today_morning_weather.get_detailed_status(),
						'icon' : weather_icons_map[today_morning_weather.get_weather_icon_name()],
						'wind' : {
							'speed' : today_morning_weather.get_wind()['speed'],
							'deg' : today_morning_weather.get_wind()['deg'],
							'speed_icon' : 'wi-beafort-'+str(int(round(today_morning_weather.get_wind()['speed']))),
							'deg_icon' : '_'+str(round_to_base(today_morning_weather.get_wind()['deg'], 15))+'-deg',
							'bad_deg' : resort.bad_wind_direction

						},
						'clouds' : today_morning_weather.get_clouds()
					}
				else: today_morning_weather_object = {}

				if today_day_weather:
					today_day_weather_object = {
						'temp' : str(today_day_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
						'temp_interval' : gettext('from')+' '+str(today_day_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C '+gettext('to')+' '+str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
						'detailed_status': today_day_weather.get_detailed_status(),
						'icon' : weather_icons_map[today_day_weather.get_weather_icon_name()],
						'wind' : {
							'speed' : today_day_weather.get_wind()['speed'],
							'deg' : today_day_weather.get_wind()['deg'],
							'speed_icon' : 'wi-beafort-'+str(int(round(today_day_weather.get_wind()['speed']))),
							'deg_icon' : '_'+str(round_to_base(today_day_weather.get_wind()['deg'], 15))+'-deg',
							'bad_deg' : resort.bad_wind_direction

						},
						'clouds' : today_day_weather.get_clouds()
					}
				else: today_day_weather_object = {}

				if today_evening_weather:
					today_evening_weather_object = {
						'temp' : str(today_evening_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
						'temp_interval' : gettext('from')+' '+str(today_evening_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C '+gettext('to')+' '+str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
						'detailed_status': today_evening_weather.get_detailed_status(),
						'icon' : weather_icons_map[today_evening_weather.get_weather_icon_name()],
						'wind' : {
							'speed' : today_evening_weather.get_wind()['speed'],
							'deg' : today_evening_weather.get_wind()['deg'],
							'speed_icon' : 'wi-beafort-'+str(int(round(today_evening_weather.get_wind()['speed']))),
							'deg_icon' : '_'+str(round_to_base(today_evening_weather.get_wind()['deg'], 15))+'-deg',
							'bad_deg' : resort.bad_wind_direction

						},
						'clouds' : today_evening_weather.get_clouds()
					}
				else: today_evening_weather_object = {}

				tomorrow_night_weather_object = {
					'temp' : str(tomorrow_night_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
					'temp_interval' : gettext('from')+' '+str(tomorrow_night_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C '+gettext('to')+' '+str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
					'detailed_status': tomorrow_night_weather.get_detailed_status(),
					'icon' : weather_icons_map[tomorrow_night_weather.get_weather_icon_name()],
					'wind' : {
						'speed' : tomorrow_night_weather.get_wind()['speed'],
						'deg' : tomorrow_night_weather.get_wind()['deg'],
						'speed_icon' : 'wi-beafort-'+str(int(round(tomorrow_night_weather.get_wind()['speed']))),
						'deg_icon' : '_'+str(round_to_base(tomorrow_night_weather.get_wind()['deg'], 15))+'-deg',
						'bad_deg' : resort.bad_wind_direction

					},
					'clouds' : tomorrow_night_weather.get_clouds()
				}

				tomorrow_morning_weather_object = {
					'temp' : str(tomorrow_morning_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
					'temp_interval' : gettext('from')+' '+str(tomorrow_morning_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C '+gettext('to')+' '+str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
					'detailed_status': tomorrow_morning_weather.get_detailed_status(),
					'icon' : weather_icons_map[tomorrow_morning_weather.get_weather_icon_name()],
					'wind' : {
						'speed' : tomorrow_morning_weather.get_wind()['speed'],
						'deg' : tomorrow_morning_weather.get_wind()['deg'],
						'speed_icon' : 'wi-beafort-'+str(int(round(tomorrow_morning_weather.get_wind()['speed']))),
						'deg_icon' : '_'+str(round_to_base(tomorrow_morning_weather.get_wind()['deg'], 15))+'-deg',
						'bad_deg' : resort.bad_wind_direction

					},
					'clouds' : tomorrow_morning_weather.get_clouds()
				}

				tomorrow_day_weather_object = {
					'temp' : str(tomorrow_day_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
					'temp_interval' : gettext('from')+' '+str(tomorrow_day_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C '+gettext('to')+' '+str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
					'detailed_status': tomorrow_day_weather.get_detailed_status(),
					'icon' : weather_icons_map[tomorrow_day_weather.get_weather_icon_name()],
					'wind' : {
						'speed' : tomorrow_day_weather.get_wind()['speed'],
						'deg' : tomorrow_day_weather.get_wind()['deg'],
						'speed_icon' : 'wi-beafort-'+str(int(round(tomorrow_day_weather.get_wind()['speed']))),
						'deg_icon' : '_'+str(round_to_base(tomorrow_day_weather.get_wind()['deg'], 15))+'-deg',
						'bad_deg' : resort.bad_wind_direction

					},
					'clouds' : tomorrow_day_weather.get_clouds()
				}

				tomorrow_evening_weather_object = {
					'temp' : str(tomorrow_evening_weather.get_temperature(unit='celsius')['temp'])+ u'\u00B0C',
					'temp_interval' : gettext('from')+' '+str(tomorrow_evening_weather.get_temperature(unit='celsius')['temp_min']) + u'\u00B0C '+gettext('to')+' '+str(current_weather.get_temperature(unit='celsius')['temp_max'])+u'\u00B0C', 
					'detailed_status': tomorrow_evening_weather.get_detailed_status(),
					'icon' : weather_icons_map[tomorrow_evening_weather.get_weather_icon_name()],
					'wind' : {
						'speed' : tomorrow_evening_weather.get_wind()['speed'],
						'deg' : tomorrow_evening_weather.get_wind()['deg'],
						'speed_icon' : 'wi-beafort-'+str(int(round(tomorrow_evening_weather.get_wind()['speed']))),
						'deg_icon' : '_'+str(round_to_base(tomorrow_evening_weather.get_wind()['deg'], 15))+'-deg',
						'bad_deg' : resort.bad_wind_direction

					},
					'clouds' : tomorrow_evening_weather.get_clouds()
				}

				result['resorts'][resort.id] = {
					'current' : current_weather_object,
					'today_night' : today_night_weather_object,
					'today_morning' : today_morning_weather_object,
					'today_day' : today_day_weather_object,
					'today_evening' : today_evening_weather_object,
					'tomorrow_night' : tomorrow_night_weather_object,
					'tomorrow_morning' : tomorrow_morning_weather_object,
					'tomorrow_day' : tomorrow_day_weather_object,
					'tomorrow_evening' : tomorrow_evening_weather_object
				}
	#except Exception as e:
	#	print str(e)
	#	print str(sys.exc_info())
	#	result = { 'success' : 'false' }
	return jsonify(result)