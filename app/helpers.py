# -*- coding: UTF-8 -*-
import string
import random

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

def round_to_base(x, base=15):
    return int(base * round(float(x)/base))

def get_randon_string_(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))