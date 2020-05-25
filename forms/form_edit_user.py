from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, ValidationError

from werkzeug.utils import secure_filename


class FormEditUser(FlaskForm):
    name = StringField('Your name or nickname', validators=[DataRequired(message='This field is required')])
    photo = FileField('Upload an image to your profile')
    submit = SubmitField('Send')

    def validate_photo(self, field):
        if field.data:
            filename = secure_filename(field.data.filename)
            if filename.rsplit('.', 1)[1] not in ('png', 'jpeg', 'jpg'):
                raise ValidationError("Invalid extension for photos, use .png or. jpeg(.jpg)")
