# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr
from app import db
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/howitworks/ [GET]
def howitworks_list(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

#for /ru/howitworks/events/
def howitworks_events(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

#for /ru/howitworks/camps/
def howitworks_camps(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

#for /ru/howitworks/resorts/
def howitworks_resorts(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

#for /ru/howitworks/locations/
def howitworks_locations(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

#for /ru/howitworks/news/
def howitworks_news(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

#for /ru/howitworks/coaches/
def howitworks_coaches(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "