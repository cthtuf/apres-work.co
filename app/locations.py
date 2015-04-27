# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_loc_id, get_curr, get_path, get_site_url
from app import db, app, cache
from models import *
from forms import SubscriptionForm
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/locations/ [GET]
@cache.cached(timeout=600)
def locations_g_list(language_suffix):
	save_lang(language_suffix)

	locations = db.session.query(Location).all()
	for loc in locations:
		loc.url = '/'+get_lang()+'/'+loc.suffix+'/'

	return render_template('g_locations.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		debug = app.debug,
		locations = locations
	)

#for /ru/spb/ [GET]
@cache.cached(timeout=600)
def locations_index(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	form = SubscriptionForm()
	return render_template('l_index.html',
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
