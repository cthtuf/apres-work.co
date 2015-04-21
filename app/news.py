# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr
from app import db
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext


#for /ru/news/ [GET]
def news_g_list(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

# /ru/spb/n/ [GET]
def news_s_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'news_list',
		language_suffix=language_suffix,
		location_suffix=location_suffix,
	))

#for /ru/spb/news/ [GET]
def news_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return "Sorry, haven't implemented yet =\ "

# /ru/spb/n/1/ [GET]
def news_s_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'news_page',
		language_suffix=language_suffix,
		location_suffix=location_suffix,
		id=id
	))


#for /ru/spb/news/1/ [GET]
def news_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return "Sorry, haven't implemented yet =\ "