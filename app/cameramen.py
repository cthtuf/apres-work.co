# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_loc_id, get_curr
from app import db, app
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/cameramen/ [GET]
def cameramen_g_list(language_suffix):
	save_lang(language_suffix)

	cameramen = Cameraman.query.all()

	return render_template('cameramen.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		rand=random.randint(1,1000000),
		cameramen=cameramen,
		debug=app.debug)


#for /ru/spb/cameramen/ [GET]
def cameramen_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)
	print 'loc_id', get_loc_id()
	cameramen = Cameraman.query.filter(Cameraman.location_id==get_loc_id()).all()

	return render_template('cameramen.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		cameramen=cameramen,
		debug=app.debug)

#for /ru/spb/cameraman/1/
def cameramen_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return "Sorry, haven't implemented yet =\ "