# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_loc_id, get_curr
from app import db, app
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext


#for /ru/riders/ [GET]
def riders_g_list(language_suffix):
	save_lang(language_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		countdown_time = 'May 14, 2015 15:03:25',
		debug=app.debug)

	riders = Rider.query.all()

	return render_template('g_riders.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		rand=random.randint(1,1000000),
		riders=riders,
		debug=app.debug)

#for /ru/spb/riders/ [GET]
def riders_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		countdown_time = 'May 14, 2015 15:03:25',
		debug=app.debug)
	
	riders = Rider.query.filter(Rider.location_id==get_loc_id()).all()

	return render_template('l_riders.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		riders=riders,
		debug=app.debug)


#for /ru/spb/riders/1/ [GET]
def riders_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	rider = Rider.query.filter(Rider.id==id).first()

	return render_template('p_rider.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rider=rider,
		debug=app.debug)