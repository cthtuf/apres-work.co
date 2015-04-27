# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

debug=True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'Kds8fdA(*@UJjdfsy&S*A7f65d678&SYAtd56as78'
MONGO_DBNAME = 'apresworkco'

MAILCHIMP_TOKEN = 'c3d906f578511669ed27c60ce4079630-us10'
MAILCHIMP_SUBSCRIPTION_LIST_ID = '55fafc9548'
MAILCHIMP_CAMP_L2A15_EN = 'cbed3703ea'
MAILCHIMP_CAMP_L2A15_RU = '53fad1f6f2'
MAILCHIMP_CAMP_L2A15_FR = '620ebbb42a'


OWM_KEY = '212261a0fa0f62fe41ed0a1ba84f6627'

#SERVER_NAME = 'apres-work.co:5000'

LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'ru': 'Русский'
}

BABEL_DEFAULT_LOCALE = 'en'

MAIL_SERVER = 'mail.apres-work.co'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['no-reply@apres-work.co']