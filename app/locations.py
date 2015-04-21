# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr
from app import db
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/locations/ [GET]
def locations_g_list(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

#for /ru/spb/ [GET]
def locations_index(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	form = SubscriptionForm()
	return render_template('indexpage.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		form=form,
		debug=app.debug)


# /ru/spb/subscribe/ [POST]
def locations_subscribe(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	try:
		form = SubscriptionForm()
		if form.validate_on_submit():		
			email = form.email.data
			if not email:
				return jsonify({'CODE' : '3', 'TEXT' : gettext('Set email address, please')})
			if db.session.query(Subscription).filter_by(email=email).count()>0:
				return jsonify({'CODE' : '2', 'TEXT' : gettext("You're already subscribed. Thank you!")})
			subscriber = Subscription(dt=datetime.datetime.now(), location_id=session['locations'][location_suffix], email=email)
			db.session.add(subscriber)
			mc = mailchimp.Mailchimp(app.config['MAILCHIMP_TOKEN'])
			mc.lists.subscribe(app.config['MAILCHIMP_SUBSCRIPTION_LIST_ID'], {'email': email, 'double_optin' : false, 'send_welcome' : true})
			db.session.commit()
			return jsonify({
				'CODE' : '0',
				'TEXT' : gettext("Great! You're sucessfully subscribed.")
			})
		else:
			return jsonify({'CODE' : '4', 'TEXT' : gettext("Incorrect format of the Email")})	
	except mailchimp.ListAlreadySubscribedError:
		return jsonify({'CODE' : '2', 'TEXT' : gettext("You're already subscribed. Thank you!")})
	except mailchimp.Error, e:
		return jsonify({'CODE' : '1', 'TEXT' : gettext("An error occured. Please repeat.")})
