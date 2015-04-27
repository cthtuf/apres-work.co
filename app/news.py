# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_loc_id, get_curr
from app import db, app, cache
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext


#for /ru/news/ [GET]
@cache.cached(timeout=600)
def news_g_list(language_suffix):
	save_lang(language_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		countdown_time = 'May 11, 2015 15:03:25',
		debug=app.debug)

	news = News.query.all()

	return render_template('g_news.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		rand=random.randint(1,1000000),
		news=news,
		debug=app.debug)

# /ru/spb/n/ [GET]
@cache.cached(timeout=600)
def news_s_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'news_list',
		language_suffix=language_suffix,
		location_suffix=location_suffix,
	))

#for /ru/spb/news/ [GET]
@cache.cached(timeout=600)
def news_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return render_template('not_ready.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		countdown_time = 'May 11, 2015 15:03:25',
		debug=app.debug)

	news = News.query.filter(News.location_id==get_loc_id()).all()

	return render_template('l_news.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		news=news,
		debug=app.debug)

# /ru/spb/n/1/ [GET]
@cache.cached(timeout=600)
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
@cache.cached(timeout=600)
def news_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	news = News.query.filter(News.id==id).first()

	return render_template('p_news.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		rand=random.randint(1,1000000),
		news=news,
		debug=app.debug)