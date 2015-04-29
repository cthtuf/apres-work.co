# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_loc_id, get_curr, get_site_url
from app import db, app, cache
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext
import urllib

#for /ru/resorts/
@cache.cached(timeout=600)
def resorts_g_list(language_suffix):
	save_lang(language_suffix)

	cbr = {}
	resorts = db.session.query(Resort).all() #get_loc_id()
	location = db.session.query(Location).filter(Location.suffix==get_loc()).first()
	for resort in resorts:
		share_text = resort.share_text.replace('_url_', get_site_url()+url_for('resorts_g_list', language_suffix=language_suffix)+'#id'+str(resort.id))
		share_text = share_text.encode('utf-8')
		share_text = urllib.quote(share_text)
		cbr[resort.id] = {
			'ID' : resort.id,
			'NAME' : resort.name,
			'PHONE' : resort.phone,
			'ADDRESS' : resort.address,
			'URL_SITE' : resort.url_site,
			'URL_IG' : resort.url_ig,
			'URL_VK' : resort.url_vk,
			'URL_FB' : resort.url_fb,
			'URL_IMG': resort.url_img,
			'LA' : resort.la,
			'LO' : resort.lo,
			'OWM_ID' : resort.owm_id,
			'DESCRIPTION' : resort.description,
			'SHARE_TEXT' : share_text,
			'CAMERAS' : []
		}
	webcameras = db.session.query(Resort, Webcamera).join(Webcamera).all()
	for camera in webcameras:
		cbr[camera.Resort.id]['CAMERAS'].append({
				'ID' : camera.Webcamera.id,
				'NAME' : camera.Webcamera.name,
				'IMG_LINK' : camera.Webcamera.img_link,
				'IFRAME_LINK' : camera.Webcamera.iframe_link,
				'IMG_NA' : camera.Webcamera.img_na,
				'LOAD_FROM_IFRAME' : camera.Webcamera.load_from_iframe
			})
	return render_template('g_resorts.html',
		language_suffix = language_suffix,
		location_suffix = get_loc(),
		resorts = cbr,
		location_header = 'All resorts',
		location_subheader = 'List of all resorts',
		rand=random.randint(1,1000000),
		debug=app.debug)

# /ru/spb/r/ [GET]
@cache.cached(timeout=600)
def resorts_s_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'resorts',
		language_suffix=language_suffix,
		location_suffix=location_suffix
	))

# /ru/spb/resorts/ [GET]
#@cache.cached(timeout=600)
def resorts_list(language_suffix, location_suffix):
	save_lang(language_suffix)
	save_loc(location_suffix)

	cbr = {}
	resorts = db.session.query(Resort).filter(Resort.location_id==get_loc_id()).all() #get_loc_id()
	location = db.session.query(Location).filter(Location.suffix==get_loc()).first()
	for resort in resorts:
		share_text = resort.share_text.replace('_url_', get_site_url()+url_for('resorts_s_list', language_suffix=language_suffix, location_suffix=location_suffix)+'#id'+str(resort.id))
		share_text = share_text.encode('utf-8')
		share_text = urllib.quote(share_text)
		cbr[resort.id] = {
			'ID' : resort.id,
			'NAME' : resort.name,
			'PHONE' : resort.phone,
			'ADDRESS' : resort.address,
			'URL_SITE' : resort.url_site,
			'URL_IG' : resort.url_ig,
			'URL_VK' : resort.url_vk,
			'URL_FB' : resort.url_fb,
			'URL_IMG': resort.url_img,
			'LA' : resort.la,
			'LO' : resort.lo,
			'OWM_ID' : resort.owm_id,
			'DESCRIPTION' : resort.description,
			'SHARE_TEXT' : share_text,
			'CAMERAS' : []
		}
	webcameras = db.session.query(Resort, Webcamera).join(Webcamera).filter(Resort.location_id==get_loc_id()).all()
	for camera in webcameras:
		cbr[camera.Resort.id]['CAMERAS'].append({
				'ID' : camera.Webcamera.id,
				'NAME' : camera.Webcamera.name,
				'IMG_LINK' : camera.Webcamera.img_link,
				'IFRAME_LINK' : camera.Webcamera.iframe_link,
				'IMG_NA' : camera.Webcamera.img_na,
				'LOAD_FROM_IFRAME' : camera.Webcamera.load_from_iframe
			})
	return render_template('l_resorts.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		resorts = cbr,
		location_header = location.resorts_header,
		location_subheader = location.resorts_subheader,
		rand=random.randint(1,1000000),
		debug=app.debug)

# /ru/spb/r/1/ [GET]
@cache.cached(timeout=600)
def resorts_s_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	return redirect(url_for(
		'resorts_page',
		language_suffix=language_suffix,
		location_suffix=location_suffix,
		id=id
	))

#for /ru/spb/resort/1/ [GET]
#@cache.cached(timeout=600)
def resorts_page(language_suffix, location_suffix, id):
	save_lang(language_suffix)
	save_loc(location_suffix)

	resort = db.session.query(Resort).filter(Resort.id==id).first()
	location = db.session.query(Location).filter(Location.suffix==get_loc()).first()
	share_text = resort.share_text.replace('_url_', get_site_url()+url_for('resorts_s_page', language_suffix=language_suffix, location_suffix=location_suffix, id=resort.id))
	share_text = share_text.encode('utf-8')
	share_text = urllib.quote(share_text)
	resort_obj = {
		'ID' : resort.id,
		'NAME' : resort.name,
		'PHONE' : resort.phone,
		'ADDRESS' : resort.address,
		'URL_SITE' : resort.url_site,
		'URL_IG' : resort.url_ig,
		'URL_VK' : resort.url_vk,
		'URL_FB' : resort.url_fb,
		'URL_IMG': resort.url_img,
		'LA' : resort.la,
		'LO' : resort.lo,
		'OWM_ID' : resort.owm_id,
		'DESCRIPTION' : resort.description,
		'SHARE_TEXT' : share_text,
		'HOW_TO_GET' : resort.how_to_get,
		'CAMERAS' : []
	}
	webcameras = db.session.query(Resort, Webcamera).join(Webcamera).filter(Resort.id==id).all()
	for camera in webcameras:
		resort_obj['CAMERAS'].append({
				'ID' : camera.Webcamera.id,
				'NAME' : camera.Webcamera.name,
				'IMG_LINK' : camera.Webcamera.img_link,
				'IFRAME_LINK' : camera.Webcamera.iframe_link,
				'IMG_NA' : camera.Webcamera.img_na,
				'LOAD_FROM_IFRAME' : camera.Webcamera.load_from_iframe
			})
	return render_template('p_resort.html',
		language_suffix = language_suffix,
		location_suffix = location_suffix,
		resort = resort_obj,

		rand=random.randint(1,1000000),
		debug=app.debug)