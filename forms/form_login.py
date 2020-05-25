from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class FormLogin(FlaskForm):
    email = StringField('Your email address', validators=[DataRequired(message='This field is required'), Email(message='Invalid email address')])
    password = PasswordField('Set password', validators=[DataRequired(message='This field is required')])
    remember = BooleanField('Remember me')
    submit = SubmitField('Send')
