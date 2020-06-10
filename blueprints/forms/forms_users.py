from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

from werkzeug.utils import secure_filename

from data import db_session
from data.model_users import User


class FormAddUser(FlaskForm):
    name_reg = StringField('Your name or nickname', validators=[DataRequired(message='This field is required')])
    email_reg = StringField('Your email address', validators=[DataRequired(message='This field is required'), Email(message='Invalid email address')])
    password_reg = PasswordField('Set password', validators=[DataRequired(message='This field is required'),
                                                             Length(min=5, message='The password must contain at least 5 characters')])
    password_again_reg = PasswordField('Repeat password', [DataRequired(message='This field is required'), EqualTo('password_reg', message='Passwords must match')])
    show_password_reg = BooleanField('Show password')
    remember_reg = BooleanField('Remember me')
    submit_reg = SubmitField('Send')

    def validate_email_reg(self, field):
        session = db_session.create_session()
        if session.query(User.email).filter(User.email == field.data).first():
            raise ValidationError("This email already exists")


class FormEditUser(FlaskForm):
    name = StringField('Your name or nickname', validators=[DataRequired(message='This field is required')])
    photo = FileField('Image')
    submit = SubmitField('Send')

    def validate_photo(self, field):
        if field.data:
            filename = secure_filename(field.data.filename)
            if filename.rsplit('.', 1)[1] not in ('png', 'jpeg', 'jpg'):
                raise ValidationError("Invalid extension for photos, use .png or. jpeg(.jpg)")


class FormLogin(FlaskForm):
    email_log = StringField('Your email address', validators=[DataRequired(message='This field is required'), Email(message='Invalid email address')])
    password_log = PasswordField('Your password', validators=[DataRequired(message='This field is required')])
    show_password_log = BooleanField('Show password')
    remember_log = BooleanField('Remember me')
    submit_log = SubmitField('Send')
