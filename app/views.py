# -*- coding: UTF-8 -*-
from app import app, db, mongo, babel
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
import flask.ext.admin
import urllib
import sys
from flask.ext.babel import gettext
from pprint import pprint
import IP2Location
from functools import partial

def get_site_url():
	return u'http://apres-work.co' #to-do add support of subdomains

#def get_locale(language_suffix=''):
	
@babel.localeselector
def get_lang(language_suffix=None):
	if language_suffix != '' and language_suffix in app.config['LANGUAGES'].keys():
		lang = language_suffix
	elif hasattr(request, 'language_suffix'):
		lang = request.language_suffix
	elif session.has_key('language'):
		lang = session['language']
	elif request.cookies.get('language'):
		lang = request.cookies.get('language')
	#elif hasattr(request, 'language_suffix'):
	#	return request.language_suffix
	else:
		lang = request.accept_languages.best_match(app.config['LANGUAGES'].keys())

	return lang

def check_location(location_suffix):
	print 'check_location', location_suffix
	loc = db.session.query(Location).filter_by(suffix=location_suffix)
	if loc.count()>0:
		request.location_id = loc.first().id
		request.location_description = loc.first().description
		return True
	else:
		return False

def get_loc_id(location_suffix=None):
	return request.location_id

def get_loc(location_suffix=None):
	print 'get_loc', location_suffix
	if location_suffix:
		loc = location_suffix
		print 'in params', loc
	elif hasattr(request, 'location_suffix'):
		loc = request.location_suffix
		print 'in request', loc
	elif session.has_key('location'):
		loc = session['location']
		print 'in session', loc
	elif request.cookies.get('location'):
		loc = request.cookies.get('location')
		print 'in cookies', loc
	else:
		print 'start detecting closest loc'
		IP2LocObj = IP2Location.IP2Location()
		print 'ip2locobj created'
		IP2LocObj.open("/home/apresworkco/public_html/app/IP2LOCATION-LITE-DB5.BIN")
		#except:
		#	IP2LocObj.open("app/IP2LOCATION-LITE-DB5.BIN")
		print 'IP2Location db loaded'
		dist=lambda s,d: (s[0]-d[0])**2+(s[1]-d[1])**2
		loc_rec = IP2LocObj.get_all(request.remote_addr)
		print 'loc_rec getted', loc_rec
		locs = db.session.query(Location).all()
		locs_coords = []
		for l in locs:
			locs_coords.append((float(l.la), float(l.lo)))
		curr_loc = (float(loc_rec.latitude), float(loc_rec.longitude))
		min_coords = min(locs_coords, key=partial(dist, curr_loc))
		loc_db = db.session.query(Location).filter_by(la=min_coords[0], lo=min_coords[1]).first()
		loc = loc_db.suffix
		print 'detected', loc
	if not check_location(loc):
		abort(404)
	return loc

def save_lang(language_suffix=None):
	lang = get_lang(language_suffix=language_suffix)

	request.language_suffix = lang
	session['language'] = lang

	#if request.args.has_key('remember_lang'):
	'''
	@after_this_request
	def attach_lang_cookie(response):
		response.set_cookie('language', lang)
		return response
	'''
	return lang

def save_loc(location_suffix=None):
	print 'save_loc', location_suffix
	loc = get_loc(location_suffix=location_suffix)

	request.location_suffix = loc
	session['location'] = loc

	#if request.args.has_key('remember_loc'):
	'''
	@after_this_request
	def attach_loc_cookie(response):
		response.set_cookie('location', loc)
		return response
	'''
	return loc

def save_curr(view):
	request.current_page = view #request.endpoint

def get_curr():
	if hasattr(request, 'current_page'):
		request.current_page
	else:
		'unknown'

def get_path(lang=''):
	if lang != '':
		part = re.search('^(\/[a-z]{2}\/)(.*)', request.path)
		if part:
			return '/'+lang+'/'+part.group(2)
		else:
			return request.path
	else:
		return request.path

# /_lang_/camp/1/ -> /ru/camp/1/
def replace_lang(path, lang=''):
	if lang == '':
		lang = get_lang()
	return path.replace('_lang_', lang)

# /en/_loc_/ -> /ru/spb/
def replace_loc(path, loc=''):
	if loc == '':
		loc = get_loc()
	return path.replace('_loc_', loc)

def is_menu_active(checked_page):
    	if get_curr() == checked_page:
    		return 'active-menu'

def is_current_language(language_suffix):
	if language_suffix==request.language_suffix:
		return 'current'
	return ''

def get_img_src(path, filename_desktop, filename_mobile):
	if request.MOBILE:
		return url_for('static', filename=path+filename_mobile)
	else:
		return url_for('static', filename=path+filename_desktop)

#pass functions to junja templates
@app.context_processor
def utility_processor():
	return dict(
		is_menu_active=is_menu_active,
		is_current_language=is_current_language,
		get_img_src=get_img_src,
		get_curr_path_other_lang=get_path,
		replace_lang=replace_lang,
		replace_loc = replace_loc
	)

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt='%d.%m.%Y'):
    return date.strftime(fmt) 

# for / [GET]
def index():
	return redirect(url_for(
		'camps_page',
		language_suffix='en',#get_locale(),
		id=1
	))

# for /ru/ [GET]
def language_index(language_suffix):
	return redirect(url_for(
		'camps_page',
		language_suffix='en',
		id=1
	))

# /ru/feedback/ [GET]
def feedback(language_suffix):
	save_langloc(language_suffix=language_suffix)
	#check_suffixes(language_suffix, location_suffix)
	return "Sorry, hasn't implemented yet =\ "
