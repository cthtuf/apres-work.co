# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_loc_id, get_curr
from app import db, app, cache
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/coaches/ [GET]
@cache.cached(timeout=600)
def coaches_g_list(language_suffix):
	save_lang(language_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		countdown_time = 'May 5, 2015 15:03:25',
		debug=app.debug)

	coaches = Coach.query.all()

	return render_template('g_coaches.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		rand=random.randint(1,1000000),
		coaches=coaches,
		debug=app.debug)

#for /ru/spb/c/ [GET]
@cache.cached(timeout=600)
def coaches_s_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'coaches_list',
		language_suffix=language_suffix,
		location_suffix=location_suffix
	))

#for /ru/spb/coaches/ [GET]
@cache.cached(timeout=600)
def coaches_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		countdown_time = 'May 5, 2015 15:03:25',
		debug=app.debug)

	print 'loc_id', get_loc_id()
	coaches = Coach.query.filter(Coach.location_id==get_loc_id()).all()

	return render_template('l_coaches.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		coaches=coaches,
		debug=app.debug)

#for /ru/spb/c/1/ [GET]
@cache.cached(timeout=600)
def coaches_s_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'coaches_page',
		language_suffix=language_suffix,
		location_suffix=location_suffix,
		id=id
	))

#for /ru/spb/coach/1/ [GET]
@cache.cached(timeout=600)
def coaches_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	coach = Coach.query.filter(Coach.id==id).first()

	return render_template('l_coaches.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		coach=coach,
		debug=app.debug)