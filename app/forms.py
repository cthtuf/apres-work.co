from flask.ext.wtf import Form
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class SubscriptionForm(Form):
    email = EmailField('Email', validators=[DataRequired(), Email()])