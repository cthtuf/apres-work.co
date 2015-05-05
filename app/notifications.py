# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr, crossdomain
from app import db
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext
import sys
import json, httplib

#for /<string:language_suffix>/<string:location_suffix/getnotifications/
@crossdomain
def notifications_list(language_suffix, location_suffix):
	return jsonify({
		'lang' : language_suffix,
		'location' : location_suffix,
		'random_value' : random.randint(1,1000000)
	})

@crossdomain
def notifications_push():
	conn = httplib.HTTPSConnection('api.parse.com', 443)
	conn.connect()

	conn.request('POST', '/1/push', json.dumps({
		'channels' : ['spb', 'msk'],
		'data' : {
			'alert' : request.args['msg'] if request.args['msg'] else 'lala test'
		}
		}), { 
			'X-Parse-Application-Id' : '8NLGU1PPwCDWstnsaRObOhKlBZ53890XBPHSrAbL',
			'X-Parse-REST-API-Key' : 'CMIehNctirWktZInxCaMMoPSHklb1I7yFVp2i0HD',
			'Content-Type' : 'application/json'
		})
	result = json.loads(conn.getresponse().read())
	print result
	return result