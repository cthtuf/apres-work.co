# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr, get_path
from app import db, app, cache
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/howitworks/ [GET]
@cache.cached(timeout=600)
def howitworks_list(language_suffix):
	save_lang(language_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		countdown_time = 'May 1, 2015 15:03:25',
		debug=app.debug)

#for /ru/howitworks/events/
@cache.cached(timeout=600)
def howitworks_events(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/camps/
@cache.cached(timeout=600)
def howitworks_camps(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/resorts/
@cache.cached(timeout=600)
def howitworks_resorts(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/locations/
@cache.cached(timeout=600)
def howitworks_locations(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/news/
@cache.cached(timeout=600)
def howitworks_news(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "

#for /ru/howitworks/coaches/
@cache.cached(timeout=600)
def howitworks_coaches(language_suffix):
	save_lang(language_suffix)

	return "Sorry, hasn't implemented yet =\ "