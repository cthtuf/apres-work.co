# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr, get_path, get_data_by_lang
from app import db, app, cache
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
@cache.cached(timeout=600)
def camps_g_list(language_suffix):
	save_curr('camps_g_list')
	save_lang(language_suffix)

	camps = Camp.query.all()

	return render_template('g_camps.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		rand=random.randint(1,1000000),
		camps = camps,
		debug=app.debug)

#for /__lang__/camp/1/ [GET]
@cache.cached(timeout=60)
def camps_page(language_suffix, id):
	save_curr('camps_page')
	lang = save_lang(language_suffix)
	loc = save_loc()

	camp = Camp.query.filter(Camp.id==id).first()
	top_slides = camp.slider_block.first().slides
	top_info_block = camp.top_info_block.first()
	services_block = camp.services.first()
	staff_block = camp.staff.first()
	main_info_block = camp.main_info_block.first()
	signup_block = camp.signup_form.first()
	partners_block = camp.partners.first()
	contact_block = camp.contact_form.first()

	mailchimp_list_token = get_data_by_lang(signup_block, '_mailchimp_token', 'en')  # get_mailchimp_list_id(lang)
	mc = mailchimp.Mailchimp(app.config['MAILCHIMP_TOKEN'])
	mailchimp_form = {}
	try:
		mailchimp_form = mc.lists.merge_vars({'id' : mailchimp_list_token})
		mailchimp_form = mailchimp_form['data'][0]['merge_vars']
	except Exception, e:
		print e
	return render_template(
		'p_camp.html',
		language_suffix = lang,
		location_suffix = loc,
		camp = camp,
		top_slides = top_slides,
		top_info_block = top_info_block,
		services_block = services_block,
		staff_block = staff_block,
		main_info_block = main_info_block,
		signup_block = signup_block,
		partners_block = partners_block,
		contact_block = contact_block,
		debug=app.debug,
		mailchimp_form=mailchimp_form
	)

#for /__lang__/__loc__/camp/1/ [POST]
def camps_attend(language_suffix, id):
	save_curr('camps_attend')
	save_lang(language_suffix)

	camp = Camp.query.filter(Camp.id==id).first()
	signup_block = camp.signup_form.first()
	mailchimp_list_token = get_data_by_lang(signup_block, '_mailchimp_token', 'en')  # get_mailchimp_list_id(lang)
	
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

#for /__lang__/camp/1/feedback/ [POST]
def camps_feedback(language_suffix, id):
	#save_curr('camps_attend')
	save_lang(language_suffix)
	pass