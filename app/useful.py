# -*- coding: utf-8 -*-
from views import save_lang, save_loc, save_curr, get_lang, get_loc, get_curr
from app import db
from models import *
from flask import render_template, request, jsonify, session, abort, redirect, url_for
from datetime import datetime,timedelta
from helpers import *
from flask.ext.babel import gettext

#for /ru/useful/
def useful_list(language_suffix):
	save_lang(language_suffix)

	return "Sorry, haven't implemented yet =\ "

#for /ru/useful/1/
def useful_page(language_suffix):
	save_lang(language_suffix)
	
	return "Sorry, haven't implemented yet =\ "