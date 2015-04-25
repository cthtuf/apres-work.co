# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr, get_path
from app import db, app
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/howitworks/ [GET]
def howitworks_list(language_suffix):
	save_lang(language_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		countdown_time = 'May 1, 2015 15:03:25',
		debug=app.debug)

#for /ru/howitworks/events/
def howitworks_events(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/camps/
def howitworks_camps(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/resorts/
def howitworks_resorts(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/locations/
def howitworks_locations(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/news/
def howitworks_news(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/coaches/
def howitworks_coaches(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "