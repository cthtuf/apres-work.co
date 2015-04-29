# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr, crossdomain
from app import db
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext
import sys

#for /<string:language_suffix>/<string:location_suffix/getnotifications/
@crossdomain
def notifications_list(language_suffix, location_suffix):
	return jsonify({
		'lang' : language_suffix,
		'location' : location_suffix,
		'random_value' : random.randint(1,1000000)
	})