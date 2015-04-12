# -*- coding: UTF-8 -*-
from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, SelectField, RadioField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email


class SubscriptionForm(Form):
    email = EmailField(u'Email', validators=[DataRequired(), Email()])
