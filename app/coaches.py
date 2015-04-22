# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_loc_id, get_curr
from app import db, app
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/coaches/ [GET]
def coaches_g_list(language_suffix):
	save_lang(language_suffix)

	coaches = Coach.query.all()

	return render_template('coaches.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		rand=random.randint(1,1000000),
		coaches=coaches,
		debug=app.debug)

#for /ru/spb/c/ [GET]
def coaches_s_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'coaches_list',
		language_suffix=language_suffix,
		location_suffix=location_suffix
	))

#for /ru/spb/coaches/ [GET]
def coaches_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)
	print 'loc_id', get_loc_id()
	coaches = Coach.query.filter(Coach.location_id==get_loc_id()).all()

	return render_template('coaches.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		coaches=coaches,
		debug=app.debug)

#for /ru/spb/c/1/ [GET]
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
def coaches_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return "Sorry, haven't implemented yet =\ "