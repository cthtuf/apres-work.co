# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr, get_path
from app import db, app
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext
import mailchimp

def get_mailchimp_list_id(language_suffix):
	if language_suffix == 'ru':
		return app.config['MAILCHIMP_CAMP_L2A15_RU']
	elif language_suffix == 'fr':
		return app.config['MAILCHIMP_CAMP_L2A15_FR']
	else:
		return app.config['MAILCHIMP_CAMP_L2A15_EN']

#for /ru/camps/ [GET]
def camps_list(language_suffix):
	save_curr('camps_list')
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

#for /__lang__/camp/1/ [GET]
def camps_page(language_suffix, id):
	print "url_rule=", request.url_rule
	print "request_path=", request.path
	print "fr path = ", get_path('fr')
	save_curr('camps_page')
	lang = save_lang(language_suffix)
	loc = save_loc()

	mailchimp_list_token = get_mailchimp_list_id(language_suffix)
	mc = mailchimp.Mailchimp(app.config['MAILCHIMP_TOKEN'])
	mailchimp_form = {}
	try:
		mailchimp_form = mc.lists.merge_vars({'id' : mailchimp_list_token})
		mailchimp_form = mailchimp_form['data'][0]['merge_vars']
	except Exception, e:
		print e
	return render_template(
		'camp.html',
		language_suffix = lang,
		location_suffix = loc,
		camp_id=1,
		debug=app.debug,
		mailchimp_form=mailchimp_form
	)

#for /__lang__/__loc__/camp/1/ [POST]
def camps_attend(language_suffix, id):
	save_curr('camps_attend')
	save_lang(language_suffix)

	mailchimp_list_token = get_mailchimp_list_id(language_suffix)
	mc = mailchimp.Mailchimp(app.config['MAILCHIMP_TOKEN'])
	merge_fields = {}
	for k,v in request.form.iteritems():
		if k != 'EMAIL':
			merge_fields[k] = v

	try:
		mc.lists.subscribe(
			mailchimp_list_token,
			{ 'email': request.form['EMAIL']}, 
			merge_fields,
			double_optin=False,
			send_welcome=True,
			update_existing=True
		)

		return jsonify({'CODE' : '0', 'TEXT' : gettext("You're in! We'll call you soon to confirm details")})

	except mailchimp.ListAlreadySubscribedError:
		return jsonify({'CODE' : '2', 'TEXT' : gettext("You're already subscribed. Thank you!")})
	except mailchimp.Error, e:
		return jsonify({'CODE' : '1', 'TEXT' : gettext("An error occured. Please repeat.")})