# -*- coding: UTF-8 -*-
from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class SubscriptionForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Email()])